"""Configuration data model and related utilities."""

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import spdx_lookup
from cookiecutter.config import get_user_config
from cookiecutter.extensions import pyslugify
from pydantic import (
    AfterValidator,
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    HttpUrl,
    ValidationError,
)
from pydantic_yaml import to_yaml_file
from rich import print
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from typing_extensions import Annotated, Literal, Self, get_args, get_origin

from . import __version__


def to_spdx_license(s: str):
    if license := spdx_lookup.by_id(s):
        return license.id
    else:
        raise ValueError("Invalid SPDX license id!")


TODAY = datetime.now()

Email = Annotated[str, Field(pattern=r"^[\S]+@[\S]+\.[\S]+$")]
Orcid = Annotated[
    str,
    Field(pattern=r"^(\d{4}-){3}\d{3}(\d|X)$"),
    AfterValidator(lambda s: f"https://orcid.org/{s}"),
]
OrcidUrl = Annotated[str, Field(pattern=r"^https://orcid.org/(\d{4}-){3}\d{3}(\d|X)$")]
SemVerStr = Annotated[str, Field(pattern=r"^\d+\.\d+\.\d+$")]
SPDXLicense = Annotated[str, AfterValidator(to_spdx_license)]
MyHttpUrl = Annotated[
    HttpUrl,
    BeforeValidator(
        lambda s: f"https://{s}" if s and not str(s).startswith("https://") else s
    ),
]


class MyBaseModel(BaseModel):
    """Tweaked BaseModel to manage the template settings.

    Adds functionality to prompt user via CLI for values of fields.

    Assumes that all fields have either a default value (None is acceptable,
    even if the field it is not optional) or another nested model.

    This ensures that the object can be constructed without being complete yet.
    """

    model_config = ConfigDict(
        str_strip_whitespace=True, str_min_length=1, validate_assignment=True
    )

    def check(self):
        """Run validation on this object again."""
        self.model_validate(self.model_dump())

    @staticmethod
    def _unpack_annotation(ann):
        """Unpack an annotation from optional, raise exception if it is a non-trivial union."""
        o, ts = get_origin(ann), get_args(ann)
        is_union = o is Union
        fld_types = [ann] if not is_union else [t for t in ts if t is not type(None)]

        ret = []
        for t in fld_types:
            inner_kind = get_origin(t)
            if inner_kind is Literal:
                ret.append([a for a in get_args(t)])
            elif inner_kind is Union:
                raise TypeError("Complex nested types are not supported!")
            else:
                ret.append(t)
        return ret

    def _field_prompt(self, key: str, *, required_only: bool = False):
        """Interactive prompt for one primitive field of the object (one-shot, no retries)."""
        fld = self.model_fields[key]
        val = getattr(self, key, None)

        if required_only and not fld.is_required():
            return val

        defval = val or fld.default

        prompt_msg = f"\n[b]{key}[/b]"
        if fld.description:
            prompt_msg = f"\n[i]{fld.description}[/i]{prompt_msg}"

        ann = self._unpack_annotation(fld.annotation)
        fst, tail = ann[0], ann[1:]

        choices = fst if isinstance(fst, list) else None
        if fst is bool and not tail:
            defval = bool(defval)
            user_val = Confirm.ask(prompt_msg, default=defval)
        else:
            if not isinstance(defval, str) and defval is not None:
                defval = str(defval)
            user_val = Prompt.ask(prompt_msg, default=defval, choices=choices)

        setattr(self, key, user_val)  # assign (triggers validation)
        return getattr(self, key)  # return resulting parsed value

    def prompt_field(
        self,
        key: str,
        *,
        recursive: bool = True,
        missing_only: bool = False,
        required_only: bool = False,
    ) -> Any:
        """Interactive prompt for one field of the object.

        Will show field description to the user and pre-set the current value of the model as the default.

        The resulting value is validated and assigned to the field of the object.
        """
        val = getattr(self, key)
        if isinstance(val, MyBaseModel):
            if recursive:
                val.prompt_fields(
                    missing_only=missing_only,
                    recursive=recursive,
                    required_only=required_only,
                )
            else:  # no recursion -> just skip nested objects
                return

        # primitive case - prompt for value and retry if given invalid input
        while True:
            try:
                # prompt, parse and return resulting value
                return self._field_prompt(key, required_only=required_only)
            except ValidationError as e:
                print()
                print(Panel.fit(str(e)))
                print("[red]The provided value is not valid, please try again.[/red]")

    def prompt_fields(
        self,
        *,
        recursive: bool = True,
        missing_only: bool = False,
        required_only: bool = False,
        exclude: List[str] = None,
    ):
        """Interactive prompt for all fields of the object. See `prompt_field`."""
        excluded = set(exclude or [])
        for key in self.model_fields.keys():
            if missing_only and getattr(self, key, None) is None:
                continue
            if key not in excluded:
                self.prompt_field(
                    key,
                    recursive=recursive,
                    missing_only=True,
                    required_only=required_only,
                )


PAGES_DOMAINS = {
    "github.com": "github.io",
    "gitlab.com": "pages.gitlab.io",
    "codebase.helmholtz.cloud": "pages.hzdr.de",
    "gitlab.hzdr.de": "pages.hzdr.de",
}


class FPCConfig(MyBaseModel):
    """Our cookiecutter template configuration.

    Based on the config, a final cookiecutter directory (with cookiecutter.json etc.)
    is generated from the meta-template.
    """

    def is_default(self) -> bool:
        """Return whether the current config consists of only the defaults."""
        dump_args = dict(
            exclude_defaults=True, exclude_none=True, mode="json-compliant"
        )
        return type(self)().model_dump(**dump_args) == self.model_dump(**dump_args)

    # project-specific

    project_name: str = Field(
        None,
        description="Name of the software project (written as it should show up in e.g. documentation).",
        exclude=True,
    )
    project_description: str = Field(
        None,
        description="One-line description of the project (<= 512 characters).",
        max_length=512,
        exclude=True,
    )  # NOTE: longer description can cause problems with package building
    project_keywords: str = Field(
        None,
        description="Search keywords characterizing your project (separated by spaces).",
        exclude=True,
    )
    project_version: SemVerStr = Field(
        "0.1.0",
        description="[link=https://semver.org]Semantic version number[/link] of the project (i.e., the version to be assigned to the next release).",
        exclude=True,
    )
    project_year: int = Field(
        TODAY.year,
        description="Year when the project was initiated (for copyright notice, usually the current year for new repositories).",
        exclude=True,
    )
    project_license: SPDXLicense = Field(
        "MIT",
        description="License used for this project (must be a valid [link=https://spdx.org/licenses]SPDX license identifier[/link], such as [b]MIT[/b] or [b]GPL-3.0-only[/b]).",
    )

    # person-specific

    last_name: str = Field(
        None, description="Your last name (usually the family name)."
    )
    first_name: str = Field(
        None,
        description="Your first name(s) (and everything else before your last name).",
    )
    email: Email = Field(
        None, description="Your contact e-mail address for this project."
    )
    orcid: Optional[Union[OrcidUrl, Orcid]] = Field(
        None,
        description="Your [link=https://www.orcid.org]ORCID[/link], as a URL or the raw identifier [b]XXXX-XXXX-XXXX-XXXX[/b] (leave empty if you do not have one yet).",
    )
    affiliation: str = Field(
        None, description="Your affiliation (usually your employer or a department)."
    )
    copyright_holder: str = Field(
        None,
        description="The copyright holder of your work (usually your employer or a department).",
    )

    # technical

    # NOTE: the URL contains lots of useful information
    project_repo_url: Optional[HttpUrl] = Field(
        None,
        description="URL of the target remote repository at your git hosting service (leave empty if you did not create it yet).",
        exclude=True,
    )

    project_hoster: MyHttpUrl = Field(
        None,
        description="Domain of the hosting service used for the repository (e.g. [b]github.com[/b], [b]gitlab.com[/b] or other GitLab instance).",
    )
    project_org: str = Field(
        None,
        description="GitHub Organization, GitLab Group or Git[Hub|Lab] Username (where the remote repository is/will be located).",
    )
    project_slug: str = Field(
        None,
        description="Machine-friendly name of the project (used as technical package name, for directories, URLs, etc.).",
    )

    project_pages_domain: str = Field(
        None,
        description="Domain where the GitHub/GitLab Pages are served (e.g. github.com -> [b]github.io[/b], gitlab.com -> [b]gitlab.io[/b], helmholtz.cloud -> [b]pages.hzdr.de[/b])",
    )
    project_pages_url: MyHttpUrl = Field(
        None,
        description="URL where the project Git[Hub|Lab] Pages will be served (if you don't know yet, enter some fake URL and change it later).",
        exclude=True,
    )

    init_cli: bool = Field(
        False, description="Do you want to add example code for a CLI application?"
    )
    init_api: bool = Field(
        False, description="Do you want to add example code for a web API service?"
    )

    # derivative values (that are not be overridable by the user)

    def project_package(self) -> str:
        """Return valid Python project package name based on project slug."""
        return self.project_slug.replace("-", "_")

    def project_git_path(self) -> str:
        return f"{self.project_org}/{self.project_slug}"

    def project_clone_url(self) -> str:
        return f"git@{self.project_hoster.host}/{self.project_git_path()}.git"

    def name_email_str(self) -> str:
        """Return author string in 'firstName lastName <EMail>' format."""
        return f"{self.first_name} {self.last_name} <{self.email}>"

    def copyright_text(self) -> str:
        return f"Copyright © {self.project_year} {self.copyright_holder}"

    def copyright_line(self) -> str:
        """Return copyright line based on year and copyright holder."""
        return f"SPDX-FileCopyrightText: {self.copyright_text()}"

    # helper functions

    def is_github(self) -> bool:
        """Return whether this is GitHub (if it is not, we assume it is a GitLab)."""
        return self.project_hoster.host == "github.com"

    def infer_from_output_dir(self, path: Path):
        self.project_name = path.name
        self.project_slug = pyslugify(path.name)

    def infer_from_repo_url(self, url: Union[str, HttpUrl]):
        """Infer field values from passed repository URL."""
        self.project_repo_url = url
        repo_url: HttpUrl = self.project_repo_url

        if not repo_url.path:
            return  # URL does not look right
        base = repo_url.path[1:].split("/")
        if not len(base) > 1:
            return  # URL does not look right
        slug = base.pop()

        self.project_hoster = repo_url.host
        self.project_org = "/".join(base)
        self.project_slug = slug
        self.project_name = slug

        if pages_domain := PAGES_DOMAINS.get(self.project_hoster.host):
            self.project_pages_domain = pages_domain

        if self.project_pages_domain:
            # if the service was successfully identified, we can also prefill the project docs URL \_^v^_/
            main_group, subgroups = base[0].lower(), "/".join(base[1:]).lower()
            rest_path = "" if not subgroups else f"/{subgroups}"
            self.project_pages_url = f"https://{main_group}.{self.project_pages_domain}{rest_path}/{self.project_slug}"

    def infer_repo_url(self):
        """Infer and set repo URL from other fields."""
        url = (
            f"https://{self.project_hoster.host}/{self.project_org}/{self.project_slug}"
        )
        self.project_repo_url = url


class CookiecutterConfig(BaseModel):
    """Wrapper class to load cookiecutter configuration file.

    We use a custom section inside it for our pre-set variables,
    to avoid polluting the regular namespace or using some special prefix.
    """

    model_config = ConfigDict(extra="allow")
    # ----

    default_context: Optional[Dict[str, Any]] = {}
    fair_python_cookiecutter: FPCConfig = Field(default_factory=lambda: FPCConfig())

    @classmethod
    def config_path(cls) -> Path:
        """Location of the .cookiecutterrc on the current platform."""
        return Path("~/.cookiecutterrc").expanduser()

    @classmethod
    def load(cls, *, config_file: Path = None, default_config: bool = False) -> Self:
        """Load config from ~/.cookiecutterrc (if missing, returns defaults)."""
        try:
            dct = get_user_config(
                config_file=config_file, default_config=default_config
            )
        except AttributeError:
            # workaround for https://github.com/cookiecutter/cookiecutter/issues/1994
            # FIXME: once it is fixed in cookiecutter, update deps + remove workaround
            dct = get_user_config(config_file=config_file, default_config=True)

        return CookiecutterConfig.model_validate(dct)

    def save(self):
        """Save current config to ~/.cookiecutterrc."""
        to_yaml_file(self.config_path(), self, exclude_none=True)


class CookiecutterJson(BaseModel):
    """Model for cookiecutter.json (compiled down from the config, not type-safe).

    It contains basic and derivative fields based on user inputs that are cumbersome to construct
    via Jinja templates or ask the user (cookiecutter private fields are stretched to their limits here).
    """

    model_config = ConfigDict(extra="ignore")
    # ----
    # internal
    copy_without_render: List[str] = Field(
        ["docs/overrides", ".github"], alias="_copy_without_render"
    )
    fpc_version: str = Field(__version__, alias="_fpc_version")

    # general
    project_name: str
    project_slug: str
    project_package: str

    project_version: str
    project_description: str
    project_keywords: str

    # for correct URLs
    project_git_hoster: str
    project_git_org: str
    project_git_path: str
    project_repo_url: str
    project_clone_url: str

    # for GitHub/Lab Pages
    project_pages_domain: str
    project_pages_url: str

    # legal
    project_license: str

    copyright_holder: str
    copyright_year: str
    copyright_text: str
    copyright_line: str

    # author info
    author_affiliation: str
    author_last_name: str
    author_first_name: str
    author_email: str
    author_orcid_url: str
    author_name_email: str

    # additional settings
    init_cli: bool
    init_api: bool
    is_github: bool

    @classmethod
    def from_config(cls, conf: CookiecutterConfig) -> Self:
        pconf = conf.fair_python_cookiecutter
        ctx = dict(conf.default_context)
        ctx.update(
            dict(
                project_name=pconf.project_name,
                project_slug=pconf.project_slug,
                project_package=pconf.project_package(),
                project_version=pconf.project_version,
                project_description=pconf.project_description,
                project_keywords=pconf.project_keywords,
                project_license=pconf.project_license,
                copyright_holder=pconf.copyright_holder,
                copyright_year=str(pconf.project_year),
                copyright_text=pconf.copyright_text(),
                copyright_line=pconf.copyright_line(),
                author_affiliation=pconf.affiliation,
                author_last_name=pconf.last_name,
                author_first_name=pconf.first_name,
                author_email=pconf.email,
                author_orcid_url=pconf.orcid if pconf.orcid else "",
                author_name_email=pconf.name_email_str(),
                project_git_hoster=str(pconf.project_hoster),
                project_git_org=pconf.project_org,
                project_git_path=pconf.project_git_path(),
                project_clone_url=pconf.project_clone_url(),
                project_repo_url=str(pconf.project_repo_url),
                project_pages_domain=pconf.project_pages_domain,
                project_pages_url=str(pconf.project_pages_url),
                init_cli=pconf.init_cli,
                init_api=pconf.init_api,
                is_github=pconf.is_github(),
            )
        )
        return CookiecutterJson(**ctx)

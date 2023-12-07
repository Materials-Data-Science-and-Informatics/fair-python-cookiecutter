"""Configuration data model and related utilities."""
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import spdx_lookup
from cookiecutter.config import get_user_config
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
from rich.prompt import Prompt
from typing_extensions import Annotated, Self


def raise_(ex):
    """Raise exception (for use in lambdas)."""
    raise ex


TODAY = datetime.now()

Email = Annotated[str, Field(pattern=r"^[\S]+@[\S]+\.[\S]+$")]
Orcid = Annotated[
    str,
    Field(pattern=r"^(\d{4}-){3}\d{3}(\d|X)$"),
    AfterValidator(lambda s: f"https://orcid.org/{s}"),
]
OrcidUrl = Annotated[str, Field(pattern=r"^https://orcid.org/(\d{4}-){3}\d{3}(\d|X)$")]
SemVerStr = Annotated[str, Field(pattern=r"^\d+\.\d+\.\d+$")]
SPDXLicense = Annotated[
    str,
    AfterValidator(
        lambda s: (spdx_lookup.by_id(s) and s) or raise_(ValueError("Invalid license"))
    ),
]
DomainName = Annotated[
    HttpUrl,
    BeforeValidator(lambda s: f"https://{s}" if not s.startswith("https://") else s),
]


class MyBaseModel(BaseModel):
    """Tweaked BaseModel to manage the template settings."""

    model_config = ConfigDict(
        str_strip_whitespace=True, str_min_length=1, validate_assignment=True
    )

    def prompt_field(self, key: str, *, recursive: bool = True) -> Any:
        """Interactive prompt for one field of the object.

        Will show field description to the user and pre-set the current value of the model as the default.

        The resulting value is validated and assigned to the field of the object.
        """
        fld = self.model_fields[key]
        val = getattr(self, key, None)

        # recursive case
        if isinstance(val, MyBaseModel):
            if recursive:
                val.prompt_fields()
            # if recursion is disabled, the field is simply skipped.
            return

        # primitive case
        success = False
        while not success:
            try:
                defval = val or fld.default
                if not isinstance(defval, str) and defval is not None:
                    defval = str(defval)

                user_val = Prompt.ask(
                    f"\n[i]{fld.description}[/i]\n[b]{key}[/b]", default=defval
                )

                setattr(self, key, user_val)
                success = True
            except ValidationError as e:
                print(e)
                print("[red]The provided value is not valid, please try again.[/red]")

        return getattr(self, key)

    def prompt_fields(self, *, recursive: bool = True, exclude: List[str] = None):
        """Interactive prompt for all fields of the object. See `prompt_field`."""
        excluded = set(exclude or [])
        for key in self.model_fields.keys():
            if key not in excluded:
                self.prompt_field(key, recursive=recursive)


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
    project_year: int = Field(
        TODAY.year,
        description="Year when the project was initiated (for copyright notice, usually the current year for new repositories).",
        exclude=True,
    )
    project_version: SemVerStr = Field(
        "0.1.0",
        description="[link=https://semver.org]Semantic version number[/link] of the project (i.e., the version to be assigned to the next release).",
        exclude=True,
    )

    # organization-specific

    license: SPDXLicense = Field(
        "mit",
        description="License used for this project (must be a valid [link=https://spdx.org/licenses]SPDX license identifier[/link], such as [b]mit[/b] or [b]gpl-3.0[/b]).",
    )
    copyright_holder: str = Field(
        None,
        description="The copyright holder of your work (usually your employer or a department).",
    )
    affiliation: str = Field(
        None, description="Your affiliation (usually your employer or a department)."
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

    # technical

    # NOTE: the URL contains lots of useful information
    project_repo_url: Optional[HttpUrl] = Field(
        None,
        description="URL of the target remote repository at your git hosting service (leave empty if you did not create it yet).",
        exclude=True,
    )

    project_hoster: DomainName = Field(
        None,
        description="Domain of the hosting service used for the repository (e.g. [b]github.com[/b], [b]gitlab.com[/b] or other GitLab instance).",
    )
    project_base: str = Field(
        None,
        description="GitHub Organization, GitLab Group or Git[Hub|Lab] Username (where the remote repository is located).",
    )
    project_slug: str = Field(
        None,
        description="Machine-friendly name of the project (used as technical package name, for directories, URLs, etc.).",
    )

    project_pages_domain: str = Field(
        None,
        description="Domain where the GitHub/GitLab Pages are served (e.g. github.com -> [b]github.io[/b], gitlab.com -> [b]gitlab.io[/b], helmholtz.cloud -> [b]pages.hzdr.de[/b])",
    )
    project_pages_url: HttpUrl = Field(
        None,
        description="URL where the Git[Hub|Lab] Pages will be served.",
        exclude=True,
    )

    # derivative values

    def name_email_str(self) -> str:
        """Return author string in 'firstName lastName <EMail>' format."""
        return f"{self.first_name} {self.last_name} <{self.email}>"

    def copyright_line(self) -> str:
        """Return copyright line based on year and copyright holder."""
        return f"SPDX-FileCopyrightText: © {self.project_year} {self.copyright_holder}"

    def is_github(self) -> bool:
        """Return whether this is GitHub (if it is not, we assume it is a GitLab)."""
        return self.project_hoster.host == "github.com"

    def infer_from_repo_url(self, repo_url: HttpUrl):
        """Infer field values from passed repository URL."""
        if not repo_url.path:
            return  # URL does not look right
        base = repo_url.path[1:].split("/")
        if not len(base) > 1:
            return  # URL does not look right
        slug = base.pop()

        self.project_hoster = repo_url.host
        self.project_base = "/".join(base)
        self.project_slug = slug
        self.project_name = slug

        if pages_domain := PAGES_DOMAINS.get(self.project_hoster.host):
            self.project_pages_domain = pages_domain

        if self.project_pages_domain:
            # if the service was successfully identified, we can also prefill the project docs URL \_^v^_/
            main_group, subgroups = base[0].lower(), "/".join(base[1:]).lower()
            rest_path = "" if not subgroups else f"/{subgroups}"
            self.project_pages_url = f"https://{main_group}.{self.project_pages_domain}{rest_path}/{self.project_slug}"

    def project_package(self):
        """Return valid Python project package name based on project slug."""
        return self.project_slug.replace("-", "_")


class CookiecutterConfig(BaseModel):
    """Wrapper class to load cookiecutter configuration file.

    We use a custom section inside it for our pre-set variables,
    to avoid polluting the regular namespace or using some special prefix.
    """

    model_config = ConfigDict(extra="allow")

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

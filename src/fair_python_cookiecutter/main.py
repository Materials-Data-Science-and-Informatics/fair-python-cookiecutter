"""Main functions for controlling the template creation."""

import os
from pathlib import Path
from shutil import which
from typing import Any, Dict

from cookiecutter.main import cookiecutter

from .config import CookiecutterConfig, CookiecutterJson
from .utils import TempDir, copy_template, run_cmd


def check_prerequisites():
    needed = ["git", "python", "pip", "poetry"]
    for prg in needed:
        if not which(prg):
            print(f"Program '{prg}' was not found in your environment, cannot proceed!")
            exit(1)


def strip_yaml_header(file_contents: str):
    """Given text file contents, remove YAML header bounded by '---' lines."""
    content = file_contents.splitlines()
    startidx = 1
    if content and content[0] == "---":
        startidx += 1
        while not content[startidx - 1].startswith("---"):
            startidx += 1
    return "\n".join(content[startidx:])


def create_gl_issue_template_from_gh(proj_root: Path):
    """Given project path, create GitLab issue templates from GitHub ones."""
    gh_templates = proj_root / ".github" / "ISSUE_TEMPLATE"
    gl_templates = proj_root / ".gitlab" / "issue_templates"

    gl_templates.mkdir(parents=True, exist_ok=True)
    for file in gh_templates.glob("*"):
        with open(gl_templates / file.name, "w") as f:
            f.write(strip_yaml_header(open(file).read()))


def remove_unneeded_code(proj_root: Path, conf: CookiecutterConfig):
    """Remove code examples the user did not wish to have in the project."""
    pkg = conf.fair_python_cookiecutter.project_package()
    to_remove = []
    if not conf.fair_python_cookiecutter.init_cli:
        to_remove += [
            (proj_root / "src" / pkg / "cli.py"),
            (proj_root / "tests" / "test_cli.py"),
        ]
    if not conf.fair_python_cookiecutter.init_api:
        to_remove += [
            (proj_root / "src" / pkg / "api.py"),
            (proj_root / "tests" / "test_api.py"),
        ]
    for file in to_remove:
        if file.is_file():
            file.unlink()


def download_licenses(
    proj_root: Path, conf: CookiecutterConfig, *, force_download: bool = False
):
    """Download all needed licenses and create main LICENSE file."""
    # download licenses if no licenses dir is in the project dir
    if force_download or not (proj_root / "LICENSES").is_dir():
        # first rename temp-REUSE.toml to REUSE.toml
        if (proj_root / "temp-REUSE.toml").is_file():
            (proj_root / "temp-REUSE.toml").rename(proj_root / "REUSE.toml")
        # only install reuse/pipx if it is not found
        reuse_cmd = "reuse --suppress-deprecation download --all"
        if not which("reuse"):
            reuse_cmd = "pipx run " + reuse_cmd
            if not which("pipx"):
                run_cmd("poetry run pip install pipx", cwd=proj_root)
                reuse_cmd = "poetry run " + reuse_cmd
        # download licenses
        run_cmd(reuse_cmd, cwd=proj_root)

    # copy main license over from resulting licenses directory
    license_name = conf.fair_python_cookiecutter.project_license
    license = Path(proj_root) / "LICENSE"
    license.write_text((proj_root / "LICENSES" / f"{license_name}.txt").read_text())


def init_git_repo(tmp_root: Path, proj_root: Path):
    # NOTE: script is OS-agnostic, .bat extension is for windows, bash does not care
    post_gen_script = tmp_root / "post_gen_project.bat"
    # rewrite newlines correctly for the OS
    post_gen_script.write_text(post_gen_script.read_text(), encoding="utf-8")
    if os.name != "nt":
        run_cmd(f"bash {post_gen_script}", cwd=proj_root)
    else:
        run_cmd(f"{post_gen_script}", cwd=proj_root)


def finalize_repository(tmp_root: Path, proj_root: Path, conf: CookiecutterConfig):
    """Finalize instantiated repository based on configuration."""
    create_gl_issue_template_from_gh(proj_root)
    remove_unneeded_code(proj_root, conf)
    download_licenses(proj_root, conf)
    init_git_repo(tmp_root, proj_root)


def create_repository(
    conf: CookiecutterConfig,
    output_dir: Path,
    *,
    cc_args: Dict[str, Any] = None,
    keep_on_fail: bool = False,
) -> Path:
    """Create a new repository based on given configuration, returns resulting directory."""
    cc_json = CookiecutterJson.from_config(conf)
    cc_args = cc_args or {}

    check_prerequisites()
    with TempDir(keep=keep_on_fail) as tmp_root:
        copy_template(tmp_root, cookiecutter_json=cc_json)
        cookiecutter(
            template=str(tmp_root),  # copy of template
            no_input=True,  # if cookiecutter still needs to ask, we did a mistake
            output_dir=str(output_dir),
            accept_hooks=True,
            keep_project_on_failure=keep_on_fail,
            **cc_args,
        )
        repo_dir = output_dir / cc_json.project_slug
        finalize_repository(tmp_root, repo_dir, conf)

        return repo_dir

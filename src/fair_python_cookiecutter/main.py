"""Main functions for controlling the template creation."""
from pathlib import Path
from typing import Any, Dict

from cookiecutter.main import cookiecutter

from .config import CookiecutterConfig, CookiecutterJson
from .utils import TempDir, copy_template


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
        return repo_dir

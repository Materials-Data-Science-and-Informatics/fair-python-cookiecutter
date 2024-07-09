"""Utilities for creation of template repository instances."""

import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional
from uuid import uuid1

from importlib_resources import files
from platformdirs import user_runtime_path

from .config import CookiecutterJson


class TempDir:
    """Cross-platform temporary directory."""

    path: Path

    def __init__(self, prefix_dir: Optional[Path] = None, *, keep: bool = False):
        """Create a cross-platform temporary directory."""
        dir: Path = prefix_dir or user_runtime_path(ensure_exists=True)
        if dir and not dir.is_dir():
            raise ValueError(
                "Passed directory path does not exist or is not a directory!"
            )

        self.path = dir / f"template_{uuid1()}"
        self.path.mkdir()
        self.keep = keep

    def __enter__(self):
        """Enter context manager."""
        return self.path

    def __exit__(self, type, value, traceback):
        """Exit context manager."""
        if not self.keep:
            shutil.rmtree(self.path)


TEMPLATE_DIR = files("fair_python_cookiecutter") / "template"


def copy_template(
    tmp_dir: Optional[Path] = None, *, cookiecutter_json: CookiecutterJson = None
) -> Path:
    """Create final template based on given configuration, returns template root directory."""
    # if no config is given, use dummy default values (useful for testing)
    if not cookiecutter_json:
        with open(TEMPLATE_DIR / "cookiecutter.json", "r") as ccjson:
            ccjson_dct = json.load(ccjson)
            cookiecutter_json = CookiecutterJson.model_validate(ccjson_dct)

    # copy the meta-template (we do not fully hardcode the paths for robustness)
    template_root = None
    for path in TEMPLATE_DIR.glob("*"):
        trg_path = tmp_dir / path.name
        if path.is_dir():
            if path.name.startswith("{{ cookiecutter"):
                template_root = path

            shutil.copytree(path, trg_path)
        else:
            shutil.copyfile(path, trg_path)

    # write a fresh cookiecutter.json based on user configuration
    with open(tmp_dir / "cookiecutter.json", "w", encoding="utf-8") as f:
        f.write(cookiecutter_json.model_dump_json(indent=2, by_alias=True))

    if not template_root:
        raise RuntimeError(
            "Template root directory not identified, this must be a bug!"
        )
    return template_root


def get_venv_path() -> Optional[Path]:
    """Return path of venv, if we detect being inside one."""
    return Path(sys.prefix) if sys.base_prefix != sys.prefix else None


VENV_PATH: Optional[Path] = get_venv_path()
"""If set, the path of the virtual environment this tool is running in."""


def venv_activate_cmd(venv_path: Path):
    if platform.system() != "Windows":
        return "source " + str(venv_path / "bin" / "activate")
    else:
        return str(venv_path / "Scripts" / "activate")


def run_cmd(cmd: str, cwd: Path = None):
    subprocess.run(cmd.split(), cwd=cwd, check=True)  # noqa: S603

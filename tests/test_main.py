import subprocess
import sys

import pytest

from fair_python_cookiecutter.main import create_repository, CookiecutterConfig


def test_configured(tmp_path):
    # generate with all demo code and different license
    conf = CookiecutterConfig.load(config_file="./tests/demo.yaml")
    conf.fair_python_cookiecutter.infer_from_repo_url(
        "https://github.com/MyOrg/my-project"
    )
    DEMO_PROJ_PKG = "my_project"
    dir = create_repository(conf, tmp_path)

    # should have the code files
    assert (dir / f"src/{DEMO_PROJ_PKG}/api.py").is_file()
    assert (dir / f"src/{DEMO_PROJ_PKG}/cli.py").is_file()
    assert (dir / "tests/test_api.py").is_file()
    assert (dir / "tests/test_cli.py").is_file()
    # and the expected license (Unlicense)
    first_license_line = open(dir / "LICENSE", "r").readline()
    assert first_license_line.find("public domain") > 0


# TODO: sanity-check after generation that all main tasks work locally:
# poetry install --with docs
# poetry run poe lint --all-files
# poetry run poe test
# poetry run poe docs

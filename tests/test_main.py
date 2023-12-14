import subprocess
import sys

from fair_python_cookiecutter.main import create_repository, CookiecutterConfig
from fair_python_cookiecutter.utils import TempDir


def sanity_check_project(proj_path):
    """Sanity-check a generated project (linters, tests, doc generation)."""
    try:
        subprocess.check_output(
            "poetry install --with docs".split(), cwd=proj_path, stderr=subprocess.PIPE
        )
        subprocess.check_output(
            "poetry run poe lint --all-files".split(),
            cwd=proj_path,
            stderr=subprocess.PIPE,
        )
        subprocess.check_output(
            "poetry run poe test".split(), cwd=proj_path, stderr=subprocess.PIPE
        )
        subprocess.check_output(
            "poetry run poe docs".split(), cwd=proj_path, stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        print("exit code: {}".format(e.returncode))
        print("stderr: {}".format(e.stderr.decode(sys.getfilesystemencoding())))


# def test_defaults(tmp_path):
#     # generate with default values
#     conf = CookiecutterConfig()
#     dir = create_repository(conf, tmp_path)
#     sanity_check_project(dir)

#     # should NOT have the code files
#     assert not (dir / f"src/{DEMO_PROJ_SLUG}api.py").is_file()
#     assert not (dir / f"src/{DEMO_PROJ_SLUG}/cli.py").is_file()
#     assert not (dir / "tests/test_api.py").is_file()
#     assert not (dir / "tests/test_cli.py").is_file()
#     # and the expected license (MIT)
#     first_license_line = open(dir / "LICENSE", "r").readline()
#     assert first_license_line.find("MIT") >= 0


def test_configured(tmp_path):
    # generate with all demo code and different license
    conf = CookiecutterConfig.load(config_file="./tests/demo.yaml")
    conf.fair_python_cookiecutter.infer_from_repo_url(
        "https://github.com/MyOrg/my-project"
    )
    DEMO_PROJ_PKG = "my_project"
    dir = create_repository(conf, tmp_path)
    sanity_check_project(dir)

    # should have the code files
    assert (dir / f"src/{DEMO_PROJ_PKG}/api.py").is_file()
    assert (dir / f"src/{DEMO_PROJ_PKG}/cli.py").is_file()
    assert (dir / "tests/test_api.py").is_file()
    assert (dir / "tests/test_cli.py").is_file()
    # and the expected license (Unlicense)
    first_license_line = open(dir / "LICENSE", "r").readline()
    assert first_license_line.find("public domain") > 0

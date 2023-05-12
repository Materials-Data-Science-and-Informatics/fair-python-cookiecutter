import subprocess

import pytest
from cookiecutter.main import cookiecutter


def sanity_check_project(proj_path):
    """Sanity-check a generated project (linters, tests, doc generation)."""
    subprocess.check_call("poetry install --with docs".split(), cwd=proj_path)
    subprocess.check_call("poetry run poe lint --all-files".split(), cwd=proj_path)
    subprocess.check_call("poetry run poe test".split(), cwd=proj_path)
    subprocess.check_call("poetry run poe docs".split(), cwd=proj_path)


@pytest.fixture
def gen(tmp_path_factory):
    """Fixture to generate a project and return resulting directory.

    Project is generated in a tempdir and cleaned up after completing the tests.

    Any passed kwargs are passed through to cookiecutter (e.g. a config).
    """

    def gen_project(**cc_args):
        out_dir = tmp_path_factory.mktemp("gen_proj")

        # actual project generation
        cookiecutter(template="./", no_input=True, output_dir=out_dir, **cc_args)

        # should be unique directory
        paths = list(out_dir.iterdir())
        assert len(paths) == 1
        proj_path = paths[0]
        assert proj_path.is_dir()

        # return path e.g. for extra tests on generated project
        return proj_path

    return gen_project


def test_cookiecutter(gen):
    # generate with default values
    dir = gen()
    sanity_check_project(dir)
    # should NOT have the code files
    assert not (dir / "src/my_amazing_app/api.py").is_file()
    assert not (dir / "src/my_amazing_app/cli.py").is_file()
    assert not (dir / "tests/test_api.py").is_file()
    assert not (dir / "tests/test_cli.py").is_file()
    # and the expected license (MIT)
    first_license_line = open(dir / "LICENSE", "r").readline()
    assert first_license_line.find("MIT") >= 0

    # ----
    # generate with all demo code and different license
    dir = gen(config_file="./tests/proj1.yaml")
    sanity_check_project(dir)
    # should have the code files
    assert (dir / "src/my_amazing_app/api.py").is_file()
    assert (dir / "src/my_amazing_app/cli.py").is_file()
    assert (dir / "tests/test_api.py").is_file()
    assert (dir / "tests/test_cli.py").is_file()
    # and the expected license (Unlicense)
    first_license_line = open(dir / "LICENSE", "r").readline()
    assert first_license_line.find("public domain") > 0

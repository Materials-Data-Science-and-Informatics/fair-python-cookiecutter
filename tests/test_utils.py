import json
from fair_python_cookiecutter.utils import TempDir, copy_template

import pytest


def test_tempdir(tmp_path):
    filename = "test.txt"

    with TempDir() as dir:
        assert dir.is_dir()

        with open(dir / filename, "w") as f:
            f.write("test")

    # with defaults should cleanup by default
    assert not dir.exists()

    with TempDir(tmp_path, keep=True) as dir:
        with open(dir / filename, "w") as f:
            f.write("test")

    # with keep=True dir should not be removed
    assert (dir / filename).is_file()

    # existing prefix path is used
    with TempDir(tmp_path) as dir:
        assert dir.parent == tmp_path

    # non-existing prefix path raises ValueError
    with pytest.raises(ValueError):
        dir = TempDir(tmp_path / "invalid")


def test_copy_template(tmp_path):
    with TempDir(tmp_path, keep=True) as tmp_dir:
        cc_json = tmp_dir / "cookiecutter.json"
        copy_template(tmp_dir)
        assert (cc_json).is_file()

        # check that field names are dumped by alias
        with open(cc_json, "r") as f:
            jsondata = json.load(f)
            assert "_copy_without_render" in jsondata

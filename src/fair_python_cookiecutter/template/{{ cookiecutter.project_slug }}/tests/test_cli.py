"""Tests for the CLI."""

import pytest
from hypothesis import given
from hypothesis import strategies as st
from typer.testing import CliRunner

from {{ cookiecutter.project_package }}.cli import app

runner = CliRunner()


def test_calc_addition():
    result = runner.invoke(app, ["calc", "add", "20", "22"])

    assert result.exit_code == 0
    assert result.stdout.strip() == "Result: 42"


person_names = ["Jane", "John"]


@pytest.mark.parametrize(
    "name, formal",
    [(name, formal) for name in person_names for formal in [False, True]],
)
def test_goodbye(name: str, formal: bool):
    args = ["say", "goodbye", name]
    if formal:
        args += ["--formal"]

    result = runner.invoke(app, args)

    assert result.exit_code == 0
    assert name in result.stdout
    if formal:
        assert "good day" in result.stdout


# Example of hypothesis auto-generated inputs,
# here the names are generated from a regular expression.

# NOTE: this is not really a good regex for names!
person_name_regex = r"^[A-Z]\w+$"


@given(st.from_regex(person_name_regex))
def test_hello(name: str):
    result = runner.invoke(app, ["say", "hello", name])

    assert result.exit_code == 0
    assert f"Hello {name}" in result.stdout

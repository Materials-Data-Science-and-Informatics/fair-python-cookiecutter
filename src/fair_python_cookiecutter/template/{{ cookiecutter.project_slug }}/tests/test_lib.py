"""Test for core library."""

import pytest
from hypothesis import assume, given
from hypothesis import strategies as st

from {{ cookiecutter.project_package }}.lib import CalcOperation, calculate


def test_calculate_invalid():
    with pytest.raises(ZeroDivisionError):
        calculate(CalcOperation.divide, 123, 0)

    with pytest.raises(ValueError):
        calculate("invalid", 123, 0)  # type: ignore

    with pytest.raises(NotImplementedError):
        calculate(CalcOperation.power, 2, 3)


# Example of how hypothesis can be used to generate different
# combinations of inputs automatically:


@given(st.sampled_from(CalcOperation), st.integers(), st.integers())
def test_calculate(op, x, y):
    # assume can be used to ad-hoc filter outputs -
    # if the assumption is violated, the test instance is skipped.
    # (better: use strategy combinators for filtering)
    assume(op != CalcOperation.divide or y != 0)
    assume(op != CalcOperation.power)  # not supported

    # we basically just check that there is no exception and the type is right
    result = calculate(op, x, y)
    assert isinstance(result, int)

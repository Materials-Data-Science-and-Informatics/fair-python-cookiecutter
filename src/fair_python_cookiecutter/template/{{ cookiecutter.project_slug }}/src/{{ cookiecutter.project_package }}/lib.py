"""Core functionality of {{ cookiecutter.project_slug }}.

This module can be used directly, or the functionality can be
exposed using some other interface, such as CLI, GUI or an API.
"""

from enum import Enum


class CalcOperation(str, Enum):
    """Supported operations of `calculate`."""

    add = "add"
    multiply = "multiply"
    subtract = "subtract"
    divide = "divide"
    power = "power"


def calculate(op: CalcOperation, x: int, y: int):
    """Calculate result of an operation on two integer numbers."""
    if not isinstance(op, CalcOperation):
        raise ValueError(f"Unknown operation: {op}")

    if op == CalcOperation.add:
        return x + y
    elif op == CalcOperation.multiply:
        return x * y
    elif op == CalcOperation.subtract:
        return x - y
    elif op == CalcOperation.divide:
        return x // y

    err = f"Operation {op} is not implemented!"
    raise NotImplementedError(err)

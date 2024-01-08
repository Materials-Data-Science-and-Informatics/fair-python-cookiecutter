"""Top level module of the project."""
from importlib.metadata import version
from typing import Final

# Set version, it will use version from pyproject.toml if defined
__version__: Final[str] = version(__package__ or __name__)

"""somesy package."""

from typing import Final

import importlib_metadata

# Set version, it will use version from pyproject.toml if defined
__version__: Final[str] = importlib_metadata.version(__package__ or __name__)

"""somesy package."""
import importlib_metadata

# Set version, it will use version from pyproject.toml if defined
__version__: str = importlib_metadata.version(__package__ or __name__)

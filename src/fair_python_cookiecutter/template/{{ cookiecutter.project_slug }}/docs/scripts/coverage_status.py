"""Mkdocs hook to run tests with coverage collection and generate a badge."""
import logging
from io import StringIO
from pathlib import Path

import anybadge
import pytest
from coverage import Coverage

log = logging.getLogger("mkdocs")


badge_colors = {
    20.0: "red",
    40.0: "orange",
    60.0: "yellow",
    80.0: "greenyellow",
    90.0: "green",
}
"""Colors for overall coverage percentage (0-100)."""


def on_pre_build(config):  # noqa
    """Generate coverage report if it is missing and create a badge."""
    if not Path("htmlcov").is_dir() or not Path(".coverage").is_file():
        log.info("Missing htmlcov or .coverage, running pytest to collect.")
        pytest.main(["--cov", "--cov-report=html"])
    else:
        log.info("Using existing coverage data.")

    cov = Coverage()
    cov.load()
    cov_percent = int(cov.report(file=StringIO()))
    log.info(f"Test Coverage: {cov_percent}%, generating badge.")

    badge = anybadge.Badge(
        "coverage",
        cov_percent,
        value_prefix=" ",
        value_suffix="% ",
        thresholds=badge_colors,
    )

    badge_svg = Path("docs/coverage_badge.svg")
    if badge_svg.is_file():
        badge_svg.unlink()
    badge.write_badge(badge_svg)

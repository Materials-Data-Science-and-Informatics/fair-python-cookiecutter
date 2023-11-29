"""Main entry point for the somesy CLI."""
import logging

import typer
from cookiecutter.config import get_user_config

logger = logging.getLogger("fair_python_cookiecutter")

app = typer.Typer()


@app.command()
def main():
    """Main entry point for creating a project from the template."""
    typer.echo("hello world!")

    conf = get_user_config()
    print(conf.get("fair-python-cookiecutter"))

"""Main entry point for the somesy CLI."""
import logging

import typer
from rich import print
from rich.prompt import Confirm
from rich.rule import Rule

from . import __version__
from .config import CookiecutterConfig

logger = logging.getLogger("fair_python_cookiecutter")

app = typer.Typer()


@app.command()
def main():
    """Create a new project from the template."""
    ccconf = CookiecutterConfig.load()

    print(Rule(title=f"[b]FAIR Python Cookiecutter[/b] {__version__}"))

    if ccconf.fair_python_cookiecutter.is_default():
        ccconf.save()  # will save the settings with default values
        print(
            "[b]Welcome![/b] It looks like this is the first time you are using this tool."
        )
        print()
        print(
            "Before creating a new software repository, please answer or confirm some questions."
        )
        print(
            "The provided information is used to fine-tune the template to your needs and environment."
        )
        print()
        print(
            "After answering all questions you will have the option the save the answers for the next time."
        )

    print(
        "If you have already created an existing remote repository for this project\n"
        "on GitHub or a GitLab instance, please provide the repository URL now ([b]recommended[/b]),\n"
        "this can simplify the initialization process. Otherwise, just leave the following field empty."
    )
    repo_url = ccconf.fair_python_cookiecutter.prompt_field("project_repo_url")
    if repo_url:
        # pre-fill default values based on remote repo URL, if given
        ccconf.fair_python_cookiecutter.infer_from_repo_url(repo_url)
    # go through all the fields, with loaded + inferred default values
    ccconf.fair_python_cookiecutter.prompt_fields(exclude=["project_repo_url"])

    print()
    save = Confirm.ask(
        "Do you want to save these settings for the next time?", default=False
    )
    if save:
        ccconf.save()
        print()
        print(f"[i]Your settings were saved in {ccconf.config_path()} ![/i]")

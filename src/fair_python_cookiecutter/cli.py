"""Main entry point for the somesy CLI."""
import logging

import typer
from rich import print
from rich.panel import Panel
from rich.prompt import Confirm
from rich.rule import Rule

from . import __version__
from .config import CookiecutterConfig

logger = logging.getLogger("fair_python_cookiecutter")

app = typer.Typer()


FIRST_TIME_NOTE = """[b]Welcome![/b] It looks like this is the first time you are using this tool.

Before creating a new software repository, please answer some questions about your project.
The information you provide is used to fine-tune the template to your needs and environment.

After answering all questions you will have the option the save the answers for the next time."""

REPO_URL_NOTE = """[b]Tip:[/b] If you have already created an existing remote repository for this project on
GitHub or a GitLab instance, you can provide the repository URL now ([b]recommended[/b])
to simplify the initialization process. Otherwise, just leave the following field empty."""

SAVE_QUESTION = """[i]Many of the values not specific to this project can be saved for next time,
so you do not have to enter them again (but you will be asked to confirm).[/i]
Do you want to save these settings?"""


@app.command()
def main():
    """Create a new project from the template."""
    print(Rule(title=f"[b]FAIR Python Cookiecutter[/b] {__version__}"))

    ccconf = CookiecutterConfig.load()
    first_time = ccconf.fair_python_cookiecutter.is_default()
    if first_time:
        print(Panel.fit(FIRST_TIME_NOTE))
        print(Panel.fit(REPO_URL_NOTE))

    # pre-fill default values based on remote repo URL, if given
    repo_url = ccconf.fair_python_cookiecutter.prompt_field("project_repo_url")
    if repo_url:
        ccconf.fair_python_cookiecutter.infer_from_repo_url(repo_url)
    # go through and confirm all the other fields, with loaded + inferred values
    ccconf.fair_python_cookiecutter.prompt_fields(exclude=["project_repo_url"])

    if Confirm.ask(SAVE_QUESTION, default=False):
        ccconf.save()
        print(f"\n[i]Your settings were saved in {ccconf.config_path()} ![/i]")

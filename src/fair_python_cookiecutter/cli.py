"""Main entry point for the somesy CLI."""

import logging
from pathlib import Path
from typing import Optional

import typer
from rich import print
from rich.panel import Panel
from rich.prompt import Confirm
from rich.rule import Rule
from typing_extensions import Annotated

from . import __version__
from .config import CookiecutterConfig, CookiecutterJson
from .main import create_repository

logger = logging.getLogger("fair_python_cookiecutter")

app = typer.Typer()


FIRST_TIME_NOTE = """[b]Welcome![/b] It looks like this is the first time you are using this tool.

Before creating a new software repository, please answer some questions about your project.
The information you provide is used to fine-tune the template to your needs and environment.

After answering all questions you will have the option the save the answers for the next time."""

REPO_URL_NOTE = """[b]Tip:[/b] If you have already created an existing remote repository for this project on
GitHub or a GitLab instance, you can provide the repository URL now ([b]recommended[/b])
to simplify the initialization process. Otherwise, just leave the following field empty."""

SAVE_QUESTION = """\n[i]Many of the values not specific to this project can be saved for next time,
so you do not have to enter them again (but you will be asked to confirm).[/i]
Do you want to save these settings?"""


def infer_from_args(
    ccconf: CookiecutterConfig, repo_url: str = "", output_dir: Optional[Path] = None
):
    """Infer some values based on passed CLI arguments, returns output_dir value."""
    if repo_url:
        ccconf.fair_python_cookiecutter.infer_from_repo_url(repo_url)
    if output_dir:
        ccconf.fair_python_cookiecutter.infer_from_output_dir(output_dir)
        return output_dir.parent
    return Path(".")


def prompt_config(ccconf: CookiecutterConfig):
    """Prompt user to confirm or update all values set for template variables."""
    # ask user for a repo url first if missing (can extract lots of info from it)
    repo_url = ccconf.fair_python_cookiecutter.project_repo_url
    if not repo_url:
        repo_url = ccconf.fair_python_cookiecutter.prompt_field("project_repo_url")
    # pre-fill default values based on remote repo URL, if provided
    if repo_url:
        ccconf.fair_python_cookiecutter.infer_from_repo_url(repo_url)
    # go through and confirm all the other fields, with loaded + inferred values
    ccconf.fair_python_cookiecutter.prompt_fields(exclude=["project_repo_url"])
    # infer URL from provided information if it was not given at some point
    if not ccconf.fair_python_cookiecutter.project_repo_url:
        ccconf.fair_python_cookiecutter.infer_repo_url()


@app.command()
def main(
    dry_run: bool = False,
    no_input: bool = False,
    config_file: Annotated[
        Optional[Path], typer.Option(file_okay=True, readable=True)
    ] = None,
    repo_url: str = "",
    output_dir: Annotated[
        Optional[Path],
        typer.Argument(
            dir_okay=False,
            file_okay=False,
            resolve_path=True,
        ),
    ] = None,
    keep_project_on_failure: bool = False,
):
    """Create a new project from the template."""
    print(Rule(title=f"[b]FAIR Python Cookiecutter[/b] {__version__}"))

    # load config (.cookiecutterrc if it exists, or defaults)
    ccconf = CookiecutterConfig.load(config_file=config_file)

    if ccconf.fair_python_cookiecutter.is_default():
        # show info for new users
        print(Panel.fit(FIRST_TIME_NOTE))
        print(Panel.fit(REPO_URL_NOTE))

    # infer values
    output_dir = infer_from_args(ccconf, repo_url=repo_url, output_dir=output_dir)

    if not no_input:
        # confirm / complete values
        prompt_config(ccconf)

        if not dry_run and Confirm.ask(SAVE_QUESTION, default=False):
            # update config
            ccconf.save()
            print(f"\n[i]Your settings were saved in {ccconf.config_path()} ![/i]")

    # check values after all the tweaking
    ccconf.fair_python_cookiecutter.check()

    if dry_run:
        # show and exit
        print(f"output_dir={output_dir}", ccconf, CookiecutterJson.from_config(ccconf))
        return

    # we're ready to create the repository
    create_repository(ccconf, output_dir, keep_on_fail=keep_project_on_failure)

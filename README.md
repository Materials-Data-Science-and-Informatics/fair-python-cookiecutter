# FAIR Python project cookiecutter template

An opinionated template to kickstart a modern Python project with FAIR metadata.

## Features

This cookiecutter sets up a skeleton for a FAIR modern Python project,
based on:

* `poetry` for packaging
* `pdoc` for generating developer documentation
* `pytest` for unit testing
* `hypothesis` for property-based testing
* `pre-commit` to orchestrate linters and formatters
* `black` for formatting
* `flake8` for linting
* `mypy` for editor-independent type-checking
* `reuse` for file-level licensing and REUSE-compliance checking
* `cffconvert` to check `CITATION.cff`

Furthermore, it provides:

* basic CI pipelines and issue templates for both GitHub and GitLab
* initial `CITATION.cff`, `codemeta.json` and `.reuse/dep5` metadata
* *Optional:* demo code (CLI with `typer` / backend API with `fastapi`)

## Requirements

`cookiecutter>=2.1`

## Usage

Run `cookiecutter URL_OF_THIS_REPOSITORY` and
follow the instructions to generate a new Python project.

If you use the template a lot, you might want to pre-configure some fields
in your `~/.cookiecutterrc`, e.g.:

```yaml
default_context:
  __org_name: "Your Institution"
  __org_mail_suffix: "your-institution.org"
  __org_rep: "Your Boss <your.boss@your-institution.org>"
  __org_gh: "Your-Github-Organization"

  author_last_name: "Lastname"
  author_first_name: "Firstname"
  author_orcid: "0000-0000-1234-5678"

```


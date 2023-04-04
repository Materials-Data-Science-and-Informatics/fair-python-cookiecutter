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

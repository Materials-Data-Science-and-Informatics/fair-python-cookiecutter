# FAIR Python project cookiecutter template

An opinionated [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template
to kickstart a modern Python project with [FAIR](https://www.go-fair.org/fair-principles/) metadata.


## Features

This cookiecutter sets up a skeleton for project that includes
* initial `CITATION.cff`, `codemeta.json` and `.reuse/dep5` metadata for citation and license information
* basic CI pipelines and issue templates for both GitHub and GitLab
* *Optional:* simple demo code (CLI with `typer` / backend API with `fastapi`)

Best practices for modern Python development are implemented by using:
* the [`src` layout](https://browniebroke.com/blog/convert-existing-poetry-to-src-layout/) to avoid many common problems
* `poetry` for dependency management and packaging
* `pytest` for unit testing
* `hypothesis` for property-based testing
* `pre-commit` to orchestrate linters and formatters
* `black` for formatting
* `autoflake` for removing unused imports
* `flake8` for linting (using various linter plugins)
* `bandit` for checking security issues in the code
* `mypy` for editor-independent type-checking
* `mkdocs` for generating documentation
* `safety` for checking security issues in the current dependencies

Metadata best practices for FAIR software are implemented using:
* `cffconvert` to check the `CITATION.cff` (citation metadata)
* `codemetapy` to generate a `codemeta.json` (software metadata)
* `reuse` to check [REUSE-compliance](https://reuse.software/spec/) (granular copyright and license metadata)
* `licensecheck` to scan for possible license incompatibilities in your dependencies


## Requirements

`cookiecutter>=2.1`

## Usage

Simply run `cookiecutter URL_OF_THIS_REPOSITORY` to generate a new Python project.

If you use the template a lot, you might want to pre-configure some template variables
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


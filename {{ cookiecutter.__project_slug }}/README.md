# {{ cookiecutter.project_name }}

![Project status](https://img.shields.io/badge/project%20status-alpha-%23ff8000)
[
![Test](https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.__project_gh_name }}/ci.yml?branch=main&label=test)
](https://github.com/{{ cookiecutter.__project_gh_name }}/actions?query=workflow:test)
[
![Coverage](https://img.shields.io/codecov/c/gh/{{ cookiecutter.__project_gh_name }})
](https://app.codecov.io/gh/{{ cookiecutter.__project_gh_name }})
[
![Docs](https://img.shields.io/badge/read-docs-success)
](https://{{ cookiecutter.project_gh_org|lower }}.github.io/metador-core/{{ cookiecutter.__project_slug }})

{{ cookiecutter.project_description }}

## :warning: Meta: Project Setup Instructions :construction:

This is a Python project bootstrapped from the
[fair-python-cookiecutter](https://jugit.fz-juelich.de/ias-9/metador/ias9-dev-general/ias9-python-cookiecutter)
template.

To get started, complete following steps:

- [ ] Inspect the generated files, check the TODO items, and adjust them as needed
- [ ] Initialize the repository with `poetry install && poetry init-dev`
- [ ] Check that everything works for local development
- [ ] Configure and push the repository and check that everything works in the CI
- [ ] Remove this section

## Getting Started

**:construction: TODO: verify that it works**

```
$ pip install git+ssh://git@github.com:{{ cookiecutter.__project_gh_name }}.git
```

## Development

This project uses [Poetry](https://python-poetry.org/) for dependency management.
You can run the following lines to setup the project for development:

```
git clone git@github.com:{{ cookiecutter.__project_gh_name }}.git
cd {{ cookiecutter.__project_slug }}
poetry install
poetry poe init-dev
```

Common tasks are accessible via [poe](https://github.com/nat-n/poethepoet):

* Use `poetry poe lint` to run linters manually, add `--all-files` to check everything.

* Use `poetry poe test` to run tests, add `--cov` to also show test coverage.

* Use `poetry poe docs` to generate local documentation.

In order to contribute, please open a pull request to the `dev` branch.
Make sure that your changes are sufficiently tested,
the documentation is up-to-date and all automatic CI pipelines succeed.

## Authors and Contributors

**:construction: TODO: list authors and contributors**

## Acknowledgements

**:construction: TODO: relevant organizational acknowledgements (employers, funders)**


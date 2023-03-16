# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## :warning: Meta: Project Setup Instructions :construction:

This is a Python project bootstrapped from the ias9-python-cookiecutter template.

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

* Use `poetry poe lint` to run the same linters manually.

* Use `poetry poe test` to run tests, add `--cov` to also show test coverage.

* Use `poetry poe docs` to generate local documentation.

In order to contribute, please open a pull request to the `dev` branch.
Make sure that your changes are sufficiently tested,
the documentation is up-to-date and all automatic CI pipelines succeed.

## [Authors and Contributors](./AUTHORS.md)

## Acknowledgements

**:construction: TODO: uncomment / add needed logos, adapt funding notice**

<div>
<img style="vertical-align: middle;" alt="FZJ Logo" src="https://github.com/Materials-Data-Science-and-Informatics/Logos/raw/main/FZJ/FZJ.png" width=30% height=30% />
&nbsp;&nbsp;
<!--
<img style="vertical-align: middle;" alt="HMC Logo" src="https://github.com/Materials-Data-Science-and-Informatics/Logos/raw/main/HMC/HMC_Logo_M.png" width=50% height=50% />
-->
</div>
<br />

This project was developed at the Institute for Materials Data Science and Informatics
(IAS-9) of the Jülich Research Center.
<!--
It was funded by the Helmholtz Metadata Collaboration (HMC),
an incubator-platform of the Helmholtz Association within the framework of the
Information and Data Science strategic initiative.
-->

[
![Docs](https://img.shields.io/badge/read-docs-success)
]({{ cookiecutter.project_pages_url }})
[
![Test Coverage]({{ cookiecutter.project_pages_url }}/main/coverage_badge.svg)
]({{ cookiecutter.project_pages_url }}/main/coverage)
{%- if cookiecutter.is_github %}
[
![CI](https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.project_git_path }}/ci.yml?branch=main&label=ci)
](https://github.com/{{ cookiecutter.project_git_path }}/actions/workflows/ci.yml)
{% endif %}

<!-- --8<-- [start:abstract] -->
# {{ cookiecutter.project_name.strip() }}

----
**:warning: TODO: Complete project setup :construction:**

This is a Python project generated from the
[fair-python-cookiecutter](https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter)
template.

**TODO:** To finalize the project setup, please carefully read and follow the instructions in the
[developer guide](https://materials-data-science-and-informatics.github.io/fair-python-cookiecutter/latest/dev_guide).
A copy of the guide is included in your project in `docs/dev_guide.md`.

----

{{ cookiecutter.project_description.strip() }}

**:construction: TODO: Write a paragraph summarizing what this project is about.**

<!-- --8<-- [end:abstract] -->
<!-- --8<-- [start:quickstart] -->

## Installation

**TODO: check that the installation instructions work**

This project works with Python > 3.9.

```bash
pip install git+ssh://{{ cookiecutter.project_clone_url }}
```

## Getting Started

**TODO: provide a minimal working example**

<!-- --8<-- [end:quickstart] -->

## Troubleshooting

### When I try installing the package, I get an `IndexError: list index out of range`

Make sure you have `pip` > 21.2 (see `pip --version`), older versions have a bug causing
this problem. If the installed version is older, you can upgrade it with
`pip install --upgrade pip` and then try again to install the package.

**You can find more information on using and contributing to this repository in the
[documentation]({{ cookiecutter.project_pages_url }}/main).**

<!-- --8<-- [start:citation] -->

## How to Cite

If you want to cite this project in your scientific work,
please use the [citation file](https://citation-file-format.github.io/)
in the [repository]({{ cookiecutter.project_repo_url }}/blob/main/CITATION.cff).

<!-- --8<-- [end:citation] -->
<!-- --8<-- [start:acknowledgements] -->

## Acknowledgements

We kindly thank all
[authors and contributors]({{ cookiecutter.project_pages_url }}/latest/credits).

**TODO: relevant organizational acknowledgements (employers, funders)**

<!-- --8<-- [end:acknowledgements] -->

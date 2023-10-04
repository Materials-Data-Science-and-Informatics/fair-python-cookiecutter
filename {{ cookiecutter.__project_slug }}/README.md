[
![Docs](https://img.shields.io/badge/read-docs-success)
]({{ cookiecutter.__project_gh_pages }})
[
![CI](https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.__project_gh_name }}/ci.yml?branch=main&label=ci)
](https://github.com/{{ cookiecutter.__project_gh_name }}/actions/workflows/ci.yml)
[
![Test Coverage]({{ cookiecutter.__project_gh_pages }}/main/coverage_badge.svg)
]({{ cookiecutter.__project_gh_pages }}/main/coverage)

<!-- --8<-- [start:abstract] -->
# {{ cookiecutter.project_name.strip() }}

----
**:warning: TODO: Complete project setup :construction:**

This is a Python project generated from the
[fair-python-cookiecutter](https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter)
template.

To finalize the project setup, please complete the following steps:

- [ ] Inspect the generated project files and adjust them as needed
- [ ] Take care of the TODOs in some of the files
- [ ] Check that everything works for you locally
- [ ] Create and add an empty remote repository (GitHub/GitLab) and push to it
- [ ] Wait and check that the CI pipeline runs successfully
- [ ] Enable Github Pages for the repository (from `gh-pages` branch)
- [ ] Remove this section
----

{{ cookiecutter.project_description.strip() }}

**:construction: TODO: Write a paragraph summarizing what this project is about.**

<!-- --8<-- [end:abstract] -->
<!-- --8<-- [start:quickstart] -->

## Installation

**:construction: TODO: check that the installation instructions work**

This project works with Python > 3.8.

```
$ pip install git+ssh://git@github.com:{{ cookiecutter.__project_gh_name }}.git
```

## Getting Started


**:construction: TODO: provide a minimal working example**

<!-- --8<-- [end:quickstart] -->

## Troubleshooting

### When I try installing the package, I get an `IndexError: list index out of range`

Make sure you have `pip` > 21.2 (see `pip --version`), older versions have a bug causing
this problem. If the installed version is older, you can upgrade it with
`pip install --upgrade pip` and then try again to install the package.

**You can find more information on using and contributing to this repository in the
[documentation]({{ cookiecutter.__project_gh_pages }}/main).**

<!-- --8<-- [start:citation] -->

## How to Cite

If you want to cite this project in your scientific work,
please use the [citation file](https://citation-file-format.github.io/)
in the [repository]({{ cookiecutter.__project_gh_repo }}/blob/main/CITATION.cff).

<!-- --8<-- [end:citation] -->
<!-- --8<-- [start:acknowledgements] -->

## Acknowledgements

We kindly thank all
[authors and contributors]({{ cookiecutter.__project_gh_pages }}/latest/credits).

**:construction: TODO: relevant organizational acknowledgements (employers, funders)**

<!-- --8<-- [end:acknowledgements] -->

# Developer Guide

This guide is targeting mainly developers, maintainers and other technical contributors
and provides more information on how to work with this repository.

## Overview

### Repository Structure

Here is a *non-exhaustive* list of the most important files and directories in the repository.

*General:*

* `AUTHORS.md`: acknowledges and lists all contributors
* `CHANGELOG.md`: summarizes the changes for each version of the software for users
* `CODE_OF_CONDUCT.md`: defines the social standards that must be followed by contributors
* `CONTRIBUTING.md`: explains  how others can contribute to the project
* `README.md`: provides an overview and points to other resources

*Metadata:*

* `CITATION.cff`: metadata stating how to cite the project
* `codemeta.json`: metadata for harvesting by other tools and services
* `LICENSE`: the (main) license of the project
* `LICENSES`: copies of all licenses that apply to files in the project
* `.reuse/dep5`: granular license and copyright information for all files and directories

*Development:*

* `pyproject.toml`: project metadata, dependencies, development tool configurations
* `poetry.lock`: needed for reproducible installation of the project
* `src`: actual code provided by the project
* `tests`: all tests for the code in the project
* `mkdocs.yml`: configuration of the project website
* `docs`: most contents used for the project website

*Automation and Quality Control:*

* `.pre-commit-config.yaml`: quality assurance tools used in the project
* `.github/workflows`: CI scripts for GitHub (QA, documentation and package deployment)
* `.github/ISSUE_TEMPLATE`: templates for the GitHub issue tracker
* `.gitlab-ci.yml`: mostly equivalent CI scripts, but for GitLab
* `.gitlab/issue_templates`: The same issues templates, but for GitLab

### Used Tools

Here is a *non-exhaustive* list of the most important tools used in the project.

Best practices for modern Python development are implemented by using:

* `poetry` for dependency management and packaging
* `pytest` for unit testing
* `hypothesis` for property-based testing
* `pre-commit` for orchestrating linters, formatters and other utilities
* `black` for source-code formatting
* `autoflake` for automatically removing unused imports
* `flake8` for general linting (using various linter plugins)
* `pydocstyle` for checking docstring conventions
* `interrogate` for computing docstring coverage
* `mypy` for editor-independent type-checking
* `mkdocs` for generating the project documentation website
* `bandit` for checking security issues in the code
* `safety` for checking security issues in the current dependencies

Metadata best practices for FAIR software are implemented using:

* `cffconvert` to check the `CITATION.cff` (citation metadata)
* `codemetapy` to generate a `codemeta.json` (general software metadata)
* `reuse` to check [REUSE-compliance](https://reuse.software/spec/) (granular copyright and license metadata)
* `licensecheck` to scan for possible license incompatibilities in the dependencies

## Basics

The project

* heavily uses `pyproject.toml`, which is a [recommended standard](https://peps.python.org/pep-0621/)
* adopts the [`src` layout](https://browniebroke.com/blog/convert-existing-poetry-to-src-layout/), to avoid [common problems](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
* keeps the actual code (`src`) and test code (`tests`) separated

The `pyproject.toml` is the **main configuration file** for the project. It contains both
general information about the software as well as configuration for various tools.

In older software, most of this information is often scattered over many little
tool-specific configuration files and a `setup.py`, `setup.cfg` and/or `requirements.txt`
file.

In this project, `pyproject.toml` is the first place that should be checked
when looking for the configuration of some development tool.

### Configuration

The main tool needed to manage and configure the project is [Poetry](https://python-poetry.org).

**Please follow its setup documentation to install it correctly.** Poetry should **not**
be installed with `pip` like other Python tools.

Poetry performs many important tasks:

* it manages the **virtual environment(s)** used for the project
* it manages all the **dependencies** needed for the code to work
* it takes care of **packaging** the code into a `pip`-installable package

You can find a cheatsheet with the most important commands
[here](https://vikasz.hashnode.dev/python-poetry-cheatsheet)
and consult its official documentation for detailed information.

Note that `poetry` is only needed for development of the repository.
The *end-users* who just want to *install and use* this project
do **not need** to set up or know anything about poetry.

Note that if you use `poetry shell` and the project is installed with `poetry install`,
in the following you do not have to prepend `poetry run` to commands you will see below.

### Task Runner

It is a good practice to have a common way for launching different project-related tasks.
It removes the need of remembering flags for various tools, and avoids duplication
of the same commands in the CI pipelines. If something in a workflow needs to change,
it can be changed in just one place, thus reducing the risk of making a mistake.

Often projects use a shell script or `Makefile` for this purpose. This project uses
[poethepoet](https://github.com/nat-n/poethepoet), as it integrates nicely with `poetry`.
The tasks are defined in `pyproject.toml` and can be launched using:

```
poetry run poe TASK_NAME
```

### CI Workflows

The project contains CI workflows for both GitHub and GitLab.

The main CI pipeline runs on each new pushed commit and will

1. Run all configured code analysis tools,
2. Run code tests with multiple versions of Python,
3. build and deploy the online project documentation website, and
4. *if a new version tag was pushed,* launch the release workflow

## Quality Control

### Static Analysis

Except for code testing, most tools for quality control are added to the project as
[`pre-commit`](https://pre-commit.com/) *hooks*. The `pre-commit` tool takes care of
installing, updating and running the tools according to the configuration in the
`.pre-commit-config.yaml` file.

For every new copy of the repository (e.g. after `git clone`), `pre-commit` first must
be activated. This is usually done using `pre-commit install`, which also requires that
`pre-commit` is already available. For more convenience, we simplified the procedure.

In this project, you can run:

```
poetry run poe init-dev
```

This will make sure that `pre-commit` is enabled in your repository copy.

Once enabled,
**every time** you try to `git commit` some **changed files**
various tools will run on those (and only those) files.

This means that (with some exceptions) `pre-commit` by default will run only
on the changed files that were added to the next commit
(i.e., files in the git *staging area*).
These files are usually colored in *green* when running `git status`.

* Some tools only *report* the problems they detected
* Some tools actively *modify* files (e.g., fix formatting)

In any case, the `git commit` will **fail** if a file was modified by a tool, or some
problems were reported. In order to complete the commit, you need to

* resolve all problems (by fixing them or marking them as false alarm), and
* `git add` all changed files **again** (to update the files in the *staging area*).

After doing that, you can retry to `git commit` your changes.

To avoid having to deal with many issues at once, it is a good habit to run
`pre-commit` by hand from time to time. In this project, this can be done with:

```
poetry run poe lint --all-files
```

### Testing

[pytest](https://docs.pytest.org/en/7.3.x/) is used as the main framework for testing.

The project uses the [`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/) plugin
to integrate `pytest` with
[`coverage`](https://coverage.readthedocs.io/en/latest/), which
collects and reports test coverage information.

In addition to writing regular unit tests with `pytest`, consider using
[hypothesis](https://hypothesis.readthedocs.io/en/latest/index.html),
which integrates nicely with `pytest` and implements *property-based testing* - which
involves automatic generation of randomized inputs for test cases. This can help to find
bugs often found for various edge cases that are easy to overlook in ad-hoc manual tests.
Such randomized tests can be a good addition to hand-crafted tests and inputs.

To run all tests, either invoke `pytest` directly, or use the provided task:

```
poetry run poe test
```

## Documentation

The project uses [`mkdocs`](https://www.mkdocs.org/) with the popular and excellent
[`mkdocs-material`](https://squidfunk.github.io/mkdocs-material/)
theme to generate the project documentation website, which provides both **user and
developer documentation**.

`mkdocs` is configured in the `mkdocs.yml` file, which we prepared in a way that there is

* **no need to duplicate sections** from files in other places (such as `README.md`)
* fully **automatic API documentation** pages based on Python docstrings in the code
* a detailed **test coverage report** is included in the website

The first point is important, because avoiding duplication means avoiding errors
whenever text or examples are updated.
The second point is convenient, as modules and functions do not need to
be added by hand, which is easy to forget.
The third point removes the need to use an external service such as
[CodeCov](https://about.codecov.io/) to store and present code coverage information.

As software changes over time and users cannot always keep up with the latest developments,
each new version of the software should provide version-specific documentation.
To make this both possible as well as convenient, this project uses
[`mike`](https://github.com/jimporter/mike) to generate and manage the `mkdocs`
**documentation for different versions** of the software.

### Online Documentation

To avoid dependence on additional services such as [readthedocs](https://readthedocs.org/),
the project website is deployed using [GitHub Pages](https://pages.github.com/).

The provided CI pipeline automatically generates the documentation for the latest
development version (i.e., current state of the `main` branch) as well as every released
version (i.e., marked by a version tag `vX.Y.Z`).

### Offline Documentation

You can manually generate a local and fully offline copy of the documentation, which
can be useful for e.g. previewing the results during active work on the documentation:

```
poetry install --with docs
poetry run poe docs
```

Once the documentation site is built, run `mkdocs serve` and
open `https://localhost:8000` in your browser to see the local copy of the website.

## Releases

From time to time the project is ready for a new **release** for users.

### Creating a New Release

Before releasing a new version, push the commit the new release should be based on
to the upstream repository, and make sure that:

* the CI pipeline completes successfully
* the version number in `pyproject.toml` is updated, in particular:
  * it must be larger than the previous released version
  * it should adequately reflect the [severity of changes](https://semver.org)
* the provided user and developer documentation is up-to-date, including:
  * a new section in the `CHANGELOG.md` file summarizing changes in the new version
  * possibly revised information about contributors and/or maintainers

If this is the case, proceed with the release by:

* creating a new tag that matches the version in the `pyproject.toml`: `git tag vX.Y.Z`
* pushing the new tag to the upstream repository: `git push origin vX.Y.Z`

The pushed version tag will trigger a pipeline that will:

* build and deploy the documentation website for the specific version
* publish the package to enabled targets (see below)

### Release Targets

Targets for releases can be enabled or disabled in `.github/workflows/ci.yml` and
configured by adapting the corresponding actions in `.github/workflows/releases.yml`.

#### Github Release

By default, the release workflow will create a basic Github Release that provides
a snapshot of the repository as a download. This requires no additional configuration.

See [here](https://github.com/softprops/action-gh-release)
for information on how the Github release can be customized.

Note that this release target is mostly for demonstration purposes.
For most Python projects, using PyPI is the recommended primary distribution method.

#### PyPI (and compatible package indices)

For releases to PyPI and Test PyPI the project uses the new
[Trusted Publishers](https://blog.pypi.org/posts/2023-04-20-introducing-trusted-publishers/)
workflow that is both more secure and convenient to use than other authorization methods.

Before the project can be released to PyPI or Test PyPI the first time,
first a [pending publisher](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/)
must be added in the PyPI account of the main project maintainer, using
`release.yml` as the requested *workflow name*.

Once this is done, set the corresponding option (`to_pypi` / `to_test_pypi`) to `true`
in the `publish` job in `ci.yml` to enable the corresponding publication target.

If the old and less secure token-based authentication method is needed or
the package should be published to a different PyPI-compatible package index, please
adapt `release.yml` [accordingly](https://github.com/pypa/gh-action-pypi-publish)).

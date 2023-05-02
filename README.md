# FAIR Python project cookiecutter template

An opinionated [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template
to kickstart a modern Python project with [FAIR](https://www.go-fair.org/fair-principles/) metadata.

## Overview

Are you a **researcher** or **research software engineer**?

Did you somehow end up developing **Python tools and libraries** as part of your job?

Are you overwhelmed and confused by the increasing demands to research software?

Regardless whether you are just planning to start a new software project, or you just
look for ideas about how you could improve its quality - **this template is for you!**

Unlike myriads of other templates, this template targets the typical case in academia -
you built some nice little tool or library for your scientific community,
and hope that others have a **good experience** - you want to provide a **quality
product** that others enjoy using. In case they actually do use it with some success, you
might also like to be acknowledged - for example, by having your tool **cited**.

To ensure quality, there are many **best practices** and recommendations for **software
development** on various levels, both general as well as Python-specific. To help others
find your project and also enable them to cite it, there are also recommendations
concerning your software project **metadata**. In fact, there are so many recommendations
that it can be hard to keep up and easy to become overwhelmed and confused.

To save you some time navigating all of that advice and figuring out how to apply it in
practice, we did the work for you and provide you with this template!

You can use it as is, adapt it, or at least get some inspiration for your projects.


## Main Features

This template sets up a skeleton for a Python project that:

* uses modern state-of-the-art development tools
* provides a baseline for professional development and maintenance
* helps following best practices for code and metadata quality
* contains detailed documentation on how to work with it

It is built to help you adopting good development practices
and follow recommendations such as:

* [DLR Software Engineering Guidelines](https://rse.dlr.de/guidelines/00_dlr-se-guidelines_en.html)
* [OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/en/criteria/0)
* innumerable other resources that can be found online

Furthermore, it implements emerging standards with the goal to improve
software metadata and make it more [FAIR](https://www.go-fair.org/fair-principles/):

* [REUSE](https://reuse.software/)
* [CITATION.cff](https://citation-file-format.github.io/)
* [CodeMeta](https://codemeta.github.io/)

Also see [this paper](https://doi.org/10.48550/arXiv.1905.08674) for an overview and
recommendations on the state of software citation in academic practice.


## Getting Started

First, make sure that you have a recent version of cookiecutter (`cookiecutter>=2.1`).
This template does not work with older versions, because they lack some needed features.

To install `cookiecutter`, you can run `pip install cookiecutter`.

To generate a new Python project, run:

```
cookiecutter URL_OF_THIS_REPOSITORY
```

If you intend to use the template a lot, e.g. if you want to use (an adaptation of)
this template as the default way to start a Python project for yourself and/or others,
you might want to configure some template variables in your `~/.cookiecutterrc`, e.g.:

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

This information will then be already pre-filled when you use the template,
saving you some time and possibly avoiding possible mistakes from manual typing.

## Overview

Before going into more detail about different topics, let us take a brief look at the body
and soul of the generated repository - various files, and tools that use or create them.

### Repository Structure

A generated project will contain *(at least)* the files and directories listed below.
Note that this is a *non-exhaustive* list, other files might be created by tools later.

*General:*

* `AUTHORS.md`: acknowledges and lists all contributors
* `CHANGELOG.md`: summarizes the changes for each version of your software for your users
* `CODE_OF_CONDUCT.md`: defines the social standards that must be followed by contributors
* `CONTRIBUTING.md`: explains in detail how others can contribute to your project
* `README.md`: starting point into the project, providing an overview and pointing to other resources

*Metadata:*

* `CITATION.cff`: metadata to cite the project or publish it as a software publication
* `codemeta.json`: metadata for other tools and services that want to understand your project
* `LICENSE`: the (main) license of your project
* `LICENSES`: contains copies of all licenses that apply to files in your project
* `.reuse/dep5`: defines license and copyright information for all files and directories

*Development:*

* `pyproject.toml`: Describes the package and its dependencies, configures development tools
* `poetry.lock`: Enables reproducible installation of your project
* `src`: All the actual code that your project consists of and will be installed by users
* `tests`: Contains all tests for the code in the repository
* `mkdocs.yml`: Configures the tool that generates your project website
* `docs`: Contains almost everything that appears on the project website
* `.gitignore`: Lists what should not be tracked by version control and possibly end up online

*Automation and Quality Control:*

* `.pre-commit-config.yaml`: Configures quality assurance tools for your project
* `.github/workflows`: CI scripts for GitHub (quality control, website generation, deployment)
* `.github/ISSUE_TEMPLATE`: Templates for the GitHub issue tracker
* `.gitlab-ci.yml`: Mostly equivalent CI scripts, but for GitLab
* `.gitlab/issue_templates`: The same templates, but for GitLab

### Used Tools

Here is a *non-exhaustive* list of the most important tools used in the generated project.

Best practices for modern Python development are implemented by using:

* `poetry` for dependency management and packaging
* `pytest` for unit testing
* `hypothesis` for property-based testing
* `pre-commit` to orchestrate linters and formatters
* `black` for formatting
* `autoflake` for removing unused imports
* `flake8` for general linting (using various linter plugins)
* `pydocstyle` for checking docstring conventions
* `interrogate` to compute docstring coverage
* `bandit` for checking security issues in the code
* `mypy` for editor-independent type-checking
* `mkdocs` for generating documentation
* `safety` for checking security issues in the current dependencies

Metadata best practices for FAIR software are implemented using:

* `cffconvert` to check the `CITATION.cff` (citation metadata)
* `codemetapy` to generate a `codemeta.json` (general software metadata)
* `reuse` to check [REUSE-compliance](https://reuse.software/spec/) (granular copyright and license metadata)
* `licensecheck` to scan for possible license incompatibilities in your dependencies

## Repository Manual

In this section we provide more details on the most important design aspects of the
generated project repository and how it is intended to be used.

### Basics

The generated project

* heavily uses `pyproject.toml`, which is a [recommended standard](https://peps.python.org/pep-0621/)
* adopts the [`src` layout](https://browniebroke.com/blog/convert-existing-poetry-to-src-layout/), to avoid [common problems](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
* keeps actual code (`src`) and test code (`tests`) separated, to avoid distributing it to normal users

The `pyproject.toml` is the central configuration file for the project. It contains both
general information about your software as well as configuration for various tools.

In older software, most of this information is often scattered over many little
tool-specific configuration files and a `setup.py`, `setup.cfg` and/or `requirements.txt`
file.

In this project, `pyproject.toml` is the first place you should check when looking for the
configuration of some development tool.

#### Package Management

The main tool needed to manage your Python project is [Poetry](https://python-poetry.org).

**Please follow its setup documentation to install it correctly.** Poetry should **not**
be installed with `pip` like other Python tools.

Poetry performs many important tasks that are often needed in a Python project:

* it manages the virtual environment used for the project, to **isolate** it from your other projects
* it manages all the **dependencies** you need for your code to work
* it helps packaging your software so others can easily install it (using `pip` or otherwise)
* it helps publishing versions of your software to a package index such as [PyPI](https://pypi.org/)

You can find a cheatsheet with the most important commands
[here](https://vikasz.hashnode.dev/python-poetry-cheatsheet)
and consult its official documentation for detailed information.

Note that `poetry` is only needed for development of the repository.
Your *end-users*, i.e. those who just want to *install and use* your project, will **not
need** to set up and learn poetry -- they can just use `pip` as usual, or whatever
installation mechanism you choose to add and support for your project.

#### Task Runner

It is a good practice to have a common way for launching different project-related tasks.
It saves you from remembering flags for various tools, and avoids the need to duplicate
the same commands in the CI pipelines. If something in your workflow needs to change, you
can change it in just one place and avoid making mistakes.

Often projects use a shell script or `Makefile` for this purpose. We use
[poethepoet](https://github.com/nat-n/poethepoet), as it integrates nicely with `poetry`.
The tasks are defined in `pyproject.toml` and can be launched using:

```
poetry run poe TASK_NAME
```

#### Quality Control

Except for code testing, most tools for quality control are added to the project as
[`pre-commit`](https://pre-commit.com/) *hooks*. The `pre-commit` tool takes care of
installing, updating and running the tools according to the configuration in the
`.pre-commit-config.yaml` file.

For every new copy of the repository (e.g. after `git clone`), `pre-commit` first must
be activated. This is usually done using `pre-commit install`, which also requires that
`pre-commit` is already available. For more convenience, we simplified the procedure.

In the generated project, you can run the task

```
poetry run poe init-dev
```

which will make sure that `pre-commit` is activated in your project repository copy.

Once activated,

* **every time** you try to `git commit` some **changed files**
* various tools will run on those (and only those) files

This means that (with some exceptions) `pre-commit` by default will run only
on the changed files that you added to the next commit (files in the git *staging area*).
These files are colored in *green* when running `git status`.

* Some tools only *report* the problems they detected
* Some tools actively *modify* files (e.g., fix formatting)

In any case, the `git commit` will **fail** if a file was modified by a tool, or some
problems were reported. In order to complete the commit, you need to

* resolve all problems (by fixing them or marking them as false alarm), and
* `git add` all changed files **again** (to update the files in the *staging area*).

After doing that, you can retry to `git commit` your changes.

To avoid having to deal with many issues at once, it is a good habit to run
`pre-commit` by hand from time to time. In the project, you can do this with:

```
poetry run poe lint --all-files
```

### Testing

[pytest](https://docs.pytest.org/en/7.3.x/) is used as the main framework for testing.

Wa use the [`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/) plugin
to integrate `pytest` with
[`coverage`](https://coverage.readthedocs.io/en/latest/), which
collects and reports test coverage information.

In addition to regular unit tests with `pytest` we *recommend to at least take a look* at
[hypothesis](https://hypothesis.readthedocs.io/en/latest/index.html),
which integrates with `pytest` and implements property-based testing - which involves
automatic generation of randomized inputs for test cases. This can help to find bugs
for edge cases you might not have thought of in your hand-written example inputs.
Depending on your project, such randomized tests can be a good addition to your
hand-crafted inputs.

To run the tests, you can invoke `pytest` directly, or use the provided task:

```
poetry run poe test
```

### Documentation

We use [`mkdocs`](https://www.mkdocs.org/) with the popular and excellent
[`mkdocs-material`](https://squidfunk.github.io/mkdocs-material/)
theme to generate the project documentation website, which provides both **user and
developer documentation**.

`mkdocs` is configured in the `mkdocs.yml` file, which we prepared in a way that you

* have **no need to duplicate sections** from files in other places (such as `README.md`)
* get fully **automatic API documentation** pages from your Python docstrings
* get your detailed **test coverage report included** into the website as well

The first point is important, because avoiding duplication means avoiding errors
whenever you update your text or examples.
The second point is convenient, because you do not have to remember to manually add a page
for a module or function by hand.
The third point is a nice feature to have, because otherwise you might be dependent on
external services such as [CodeCov](https://about.codecov.io/)
to store and present this information for you.

Your software changes and improves over time, and your documentation hopefully does too.
But if users for a reason have to use an outdated version, they should be able to find
information for the exact version they use.

To make this both possible as well as convenient, we use
[`mike`](https://github.com/jimporter/mike) to generate and manage the `mkdocs`
**documentation for different versions** of your software.

#### Building the documentation

If you use GitHub, all you need to do to get a nice project website is to enable
[GitHub Pages](https://pages.github.com/) for your repository. There is no need to use
additional service providers such as [readthedocs](https://readthedocs.org/).

The provided CI pipelines will generate the documentation for your latest version as well
as every released version and deploy them to the `gh-pages` branch whenever you push new
commits to your `main` branch. This means that your automatic API documentation will
always be up to date.

If you are actively working on the documentation and want to have a local preview
before you commit changes, or for some other reasons need a local copy, you can generate
documentation locally:

```
poetry install --with docs
poetry run poe docs
```

Once the documentation site is build, you can run `mkdocs serve` and then
open `https://localhost:8000` to browse your local documentation in your browser.

### CI Pipelines

The project contains CI pipeline scripts for both GitHub and GitLab.

The pipelines run on each new pushed commit and will

1. First run all the configured `pre-commit` hooks, and
2. if those succeed - run the code tests with multiple versions of Python, and
3. if those succeed - build/update the online project documentation website.

### Releases

From time to time you will want to publish a new version **release** for your users.

In the generated project, we assume that you want to release a new version to the main
*Python Package Index* [PyPI](https://pypi.org/), where most Python projects are listed.
This will enable users to easily install your software using `pip`.

#### Initial Preparations

In the following, we assume that you have an account at both
[PyPI](https://pypi.org/) and [Test PyPI](https://test.pypi.org/).

Setup your project on both sites and make sure to add two
[secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
called `PYPI_TOKEN` and `TEST_PYPI_TOKEN` to your repository, each containing
the corresponding token that authorizes the CI pipeline to publish a new version
of your Python project.

#### Creating a New Release

To create a new release, you should first make sure that:

* the version number in `pyproject.toml` is larger than the last released version
* the version number reflects the [severity of changes](https://semver.org)
* all quality checkers and tests complete without issues (locally and also in the CI)
* the user and developer documentation is up-to-date, including
  * a new section in the `CHANGELOG.md` file summarizing changes in the new version
  * possibly revised information about contributors and/or maintainers

If this is the case, you can proceed with the release:

* create a new tag matching the version in the `pyproject.toml`: `git tag vX.Y.Z`
* push the new tag upstream: `git push origin vX.Y.Z`

A CI pipeline, triggered by the pushed tag, will automatically:

* build the documentation page for the specific version
* deploy the package to Test PyPI

Now you can inspect your project page on Test PyPI and check that everything looks good.

TODO:
complete release flow with Github releases and PyPI

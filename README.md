# FAIR Python project cookiecutter template

An opinionated [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template
to kickstart a modern Python project with [FAIR](https://www.go-fair.org/fair-principles/) metadata.

## Overview

Are you a **researcher** or **research software engineer**?

Did you somehow end up developing **Python tools and libraries** as part of your job?

Are you overwhelmed and confused by the increasing demands to research software?

Regardless whether you are just planning to start a new software project, or you just
want some ideas about how you could improve its quality - **this template is for you!**

Unlike myriads of other templates, this template targets the typical case in academia -
you built some nice little tool or library for your scientific community,
and want that others have a **good experience** - you want to provide a **quality
product**. In case they actually use it with great success, you might also want to be
acknowledged - for example, by having your tool **cited**.

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
* is ready for professional development and maintenance
* helps following best practices for code and metadata quality

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

## Getting Started

Make sure that you have a recent version of cookiecutter (`cookiecutter>=2.1`).

This template does not work with old versions, because they lack certain features.


To generate a new Python project, simply run `cookiecutter URL_OF_THIS_REPOSITORY`.

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
and soul of the generated repository - various files and tools that need or produce them.

### Repository Structure

A generated project will contain *(at least)* the files and directories listed below.
Note that this is a non-exhaustive list, other files might be created by tools later.

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

Here is a non-exhaustive list of the most important tools used in the generated project.

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

## User Manual

### General

The generated project

* heavily uses the `pyproject.toml`, which is a [recommended standard](https://peps.python.org/pep-0621/)
* uses the [`src` layout](https://browniebroke.com/blog/convert-existing-poetry-to-src-layout/), to avoid [common problems](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
* keeps actual code (`src`) and test code (`tests`) separated, to avoid distributing it to normal users

The `pyproject.toml` is the central configuration file for the project.

It contains both general information about your software as well as configuration for
various tools. In older software, most of this information is often distributed an
many little tool-specific configuration files and a `setup.py`, `setup.cfg` or `requirements.txt` file.

The main tool to manage your project is [Poetry](https://python-poetry.org).

Take some time to learn about poetry, as it performs many important tasks:

* it manages the virtual environment used for the project, to **isolate** it from your other projects
* it manages all the **dependencies** you need for your code to work
* it helps packaging your software so others can easily install it (using `pip` or otherwise)
* it helps publishing versions of your software to a package index such as [PyPI](https://pypi.org/)

We also use [poethepoet](https://github.com/nat-n/poethepoet) as a task runner.

Other projects use a shell script or `Makefile` for a similar purpose. However this is
implemented - it is a good idea to have a central mechanism to launch different
maintenance tasks. It saves you from remembering flags for different tools, and exactly
the same commands can be easily used in the CI pipelines. If something in your workflow
needs to change, you can change it in just one place and avoid mistakes.


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


### Documentation

We use [`mkdocs`](https://www.mkdocs.org/) with the popular
[`mkdocs-material`](https://squidfunk.github.io/mkdocs-material/)
theme to generate the project documentation website, which provides both **user and
developer documentation**.

`mkdocs` is configured in the `mkdocs.yml` file, which is prepared so that you

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

On top of `mkdocs` we use [`mike`](https://github.com/jimporter/mike) to generate and
manage documentation for different versions of your software. Your software changes and
improves over time, and your documentation hopefully does too. But if users for a reason
have to use an outdated version, they should be able to find information for the exact
version they use.

#### Building the documentation


If you use GitHub, all you need to do to get a nice project website is to enable
[GitHub Pages] for your repository. So there is no need to use additional service
providers such as [readthedocs](https://readthedocs.org/).

The provided CI pipelines will generate the documentation for your latest version as well
as every released version and deploy them to the `gh-pages` branch whenever you push new
commits to your `main` branch. This means that your automatic API documentation will
always be up to date.

If you are working on other parts of the documentation and want to have a local preview
before you commit changes, or for some other reasons need a local copy, you can generate
documentation locally:

```
poetry install --with docs
poetry run poe docs
```

Run `mkdocs serve` to browse your local documentation copy
 `https://localhost:8000` in your browser.


### CI Pipelines

TODO

### Releases

TODO

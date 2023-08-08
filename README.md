[
![Docs](https://img.shields.io/badge/read-docs-success)
](https://materials-data-science-and-informatics.github.io/fair-python-cookiecutter)
[
![CI](https://img.shields.io/github/actions/workflow/status/Materials-Data-Science-and-Informatics/fair-python-cookiecutter/ci.yml?branch=main&label=ci)
](https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter/actions/workflows/ci.yml)

<!-- --8<-- [start:abstract] -->
# fair-python-cookiecutter

An opinionated cookiecutter template to kickstart a modern best-practice Python project with FAIR metadata.

*Check out a demo repository generated from this template
:point_right: [here](https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter-demo)*

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

<!-- --8<-- [end:abstract] -->

<!-- --8<-- [start:quickstart] -->

## Getting Started

First, make sure that you have a recent version of
[cookiecutter](https://www.cookiecutter.io/) (`cookiecutter>=2.1`).
This template does not work with older versions, because they lack some needed features.

To install `cookiecutter`, you can run `pip install cookiecutter`.

To generate a new Python project from this template, run:

```bash
cookiecutter https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter
```

This will spawn an interactive prompt, where you have to provide some information and select
a starting skeleton for your software project. Don't worry, you can always adapt this
information later on by hand. After this cookiecutter will initate your software project.

Your new project repository will also include a copy of a
[developer guide](https://materials-data-science-and-informatics.github.io/fair-python-cookiecutter-demo/latest/dev_guide),
containing more information about the structure and features of the generated project.
Feel free to either remove it, or keep (and possibly adjust) it as extended technical
project documentation for yourself and other future project contributors.

You can find a demo repository generated from this template [here](https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter-demo).

## Configuring the Template

If you intend to use the template a lot, e.g. if you want to use (an adaptation of)
this template as the default way to start a Python project for yourself and/or others,
you might want to configure some template variables in your `~/.cookiecutterrc`.
Here is an example cookiecutter configuration:

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

This information will be already pre-filled when you use the template,
saving you some time and possibly avoiding possible mistakes from manual typing.

## Modifying the Template

If you want to adjust it to your needs and likings (e.g. add, remove or substitute certain
tools), you probably want to
[fork](https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter/fork)
it to get your own copy. Then you can do the desired changes and use the URL of your
template repository instead of this one to kickstart your projects.

However, if you think that your changes are of general interest and would improve this
template, consider to get in touch
and [contribute](https://materials-data-science-and-informatics.github.io/fair-python-cookiecutter/main/contributing/)!

In any case we are very happy to know about any similar or derivative templates, e.g. for
more specific use-cases or based on other tool preferences.

## Reusing Parts of the Template

If you already have an existing project where you would like to introduce things you like
from this template, there are two main ways to do so:

1. move your code into a fresh repository based on this template
2. use parts of the template in your existing project structure

If your project currently has no sophisticated setup of tools or strong preferences about
them, option 1 might be the simplest way to adopt the template. Your code then needs to be
moved into the `YOUR_PROJECT/src` subdirectory.

On the other hand, if you already have a working setup that you do not wish to replace
completely, you can take a look at

* the `.pre-commit-config.yaml` file to adopt some of the quality assurance tools listed there
* the CI pipelines defined in `.github/workflows` or `.gitlab-ci.yml` for automated tests and releases
* the `mkdocs.yml` and `docs/` subdirectory to see how the project website works

<!-- --8<-- [end:quickstart] -->

<!-- --8<-- [start:citation] -->

## How to Cite

If you want to cite this project in your scientific work,
please use the [citation file](https://citation-file-format.github.io/)
in the [repository](https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter/blob/main/CITATION.cff).

<!-- --8<-- [end:citation] -->
<!-- --8<-- [start:acknowledgements] -->

## Acknowledgements

We kindly thank all
[authors and contributors](https://materials-data-science-and-informatics.github.io/fair-python-cookiecutter/latest/credits).

<div>
<img style="vertical-align: middle;" alt="HMC Logo" src="https://github.com/Materials-Data-Science-and-Informatics/Logos/raw/main/HMC/HMC_Logo_M.png" width=50% height=50% />
&nbsp;&nbsp;
<img style="vertical-align: middle;" alt="FZJ Logo" src="https://github.com/Materials-Data-Science-and-Informatics/Logos/raw/main/FZJ/FZJ.png" width=30% height=30% />
</div>
<br />

This project was developed at the Institute for Materials Data Science and Informatics
(IAS-9) of the Jülich Research Center and funded by the Helmholtz Metadata Collaboration
(HMC), an incubator-platform of the Helmholtz Association within the framework of the
Information and Data Science strategic initiative.

<!-- --8<-- [end:acknowledgements] -->

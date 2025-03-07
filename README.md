[
![Docs](https://img.shields.io/badge/read-docs-success)
](https://materials-data-science-and-informatics.github.io/fair-python-cookiecutter)
[
![CI](https://img.shields.io/github/actions/workflow/status/Materials-Data-Science-and-Informatics/fair-python-cookiecutter/ci.yml?branch=main&label=ci)
](https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter/actions/workflows/ci.yml)

<!-- --8<-- [start:abstract] -->

<br />
<div>
<img style="center-align: middle;" alt="FAIR Python Cookiecutter Logo" src="https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/Logos/main/FAIRPythonCookiecutter/FAIRPYTHONCOOKIECUTTER_Logo_Text.png" width=70% height=70% />
&nbsp;&nbsp;
</div>
<br />

# fair-python-cookiecutter

An opinionated cookiecutter template to kickstart a modern best-practice Python project with FAIR metadata.

<!-- NOTE: For technical reasons, it is much easier to use GitHub
     for hosting the mindmap than adding it to the repository -->

![FAIR Software Mindmap](https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter/assets/371708/ef566ee1-8965-4d58-9ede-18eeb49a476e)

_Check out the
[demo repository](https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter-demo)
generated from this template!_

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

-   uses modern state-of-the-art development tools
-   provides a baseline for professional development and maintenance
-   helps following best practices for code and metadata quality
-   contains detailed documentation on how to work with it

It is built to help you adopting good practices
and follow recommendations such as:

-   [DLR Software Engineering Guidelines](https://rse.dlr.de/guidelines/00_dlr-se-guidelines_en.html)
-   [OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/en/criteria/0)
-   [Netherlands eScience Center](https://fair-software.eu)
-   innumerable other resources that can be found online

Furthermore, it implements emerging standards with the goal to improve
software metadata and make it more [FAIR](https://www.go-fair.org/fair-principles/):

-   [REUSE](https://reuse.software/)
-   [CITATION.cff](https://citation-file-format.github.io/)
-   [CodeMeta](https://codemeta.github.io/)

Also see [this paper](https://doi.org/10.48550/arXiv.1905.08674) for an overview and
recommendations on the state of software citation in academic practice.

<!-- --8<-- [end:abstract] -->

<!-- --8<-- [start:quickstart] -->

## Getting Started

Make sure that you have a working Python interpreter in version at least 3.9,
`git` and [`poetry`](https://python-poetry.org/docs/#installation) installed.

To install the template, run `pip install fair-python-cookiecutter`.

Now you can use the tool to generate a new Python project:

```bash
fair-python-cookiecutter YourProjectName
```

This will spawn an interactive prompt, where you have to provide some information and
make some choices for your new software project. Don't worry, you can always adapt
everything later on by hand. After this, your software project will be created in
a new directory.

To save you some time answering the questions, we recommend that you create an empty repository
in GitHub or GitLab of your choice (i.e., the location where you plan to push your new project).

If you already have created an empty remote repository or know exactly its future
location, you can provide the URL, which already will provide many required inputs:

```bash
fair-python-cookiecutter --repo-url https://github.com/YourOrganization/YourProjectName
```

Your new project repository will also include a copy of a
[developer guide](https://materials-data-science-and-informatics.github.io/fair-python-cookiecutter-demo/latest/dev_guide),
containing more information about the structure and features of the generated project.

**Please familiarize yourself with the generated structures, files and the contents of the
developer guide.** Feel free to either remove the guide afterwards, or keep (and possibly
adjust) it as extended technical project documentation for yourself and other future
project contributors.

You can find a demo repository generated from this template [here](https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter-demo).

### Example Code

When you are creating your project, you are asked for several inputs. You can have an example CLI(Command Line Interface) and/or API(Application Programming interface) code within your new project.

Lets assume your project name is `my-awesome-project`.

You can run the CLI App with below command. For further usage, please check typer documentation.

```bash
poetry shell

# Run your CLI App
my-awesome-project-cli calculate add 5 2
```

You can run the API App with below command.

```bash
poetry shell

# Run the API program, it will be open for connection
my-awesome-project-api
```

Now, you can a tool to send a HTTP request for the API. You can open another terminal and run this command

```
# send a request that does the same thing as the CLI
curl 'http://localhost:8000/calculate/add?x=5&y=2'
```

For further usage of the API, please check fastAPI documentation.

## Configuring the Template

If you intend to use the template a lot, e.g. if you want to use (an adaptation of)
this template as the default way to start a Python project for yourself and/or others,
you might want to configure some template variables in your `~/.cookiecutterrc`.
Here is an example cookiecutter configuration:

```yaml
fair_python_cookiecutter:
    last_name: 'Carberry'
    first_name: 'Josiah'
    project_keywords: 'psychoceramics analytics'
    email: 'josiah.carberry@brown.edu'
    orcid: '0000-0002-1825-0097'
    affiliation: 'Brown University'
    copyright_holder: 'Brown University'
    license: 'MIT'
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
template for a majority of users, please get in touch
and [contribute](https://materials-data-science-and-informatics.github.io/fair-python-cookiecutter/main/contributing/)
or [suggest](https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter/issues) an improvement!

In any case we are very happy to know about any similar or derivative templates, e.g. for
more specific use-cases or based on other tool preferences.

## Reusing Parts of the Template

If you already have an existing project where you would like to introduce things you like
from this template, there are two main ways to do so:

1. move your code into a fresh repository based on this template
2. use parts of the template in your existing project structure

If your project currently has no sophisticated setup of tools or strong preferences about
them, option 1 might be the simplest way to adopt the template. Your code then needs to be
moved into the `YOUR_PROJECT/src/YOUR_PACKAGE` subdirectory.

On the other hand, if you already have a working setup that you do not wish to replace
completely, you can take a look at

-   the `.pre-commit-config.yaml` file to adopt some of the quality assurance tools listed there
-   the CI pipelines defined in `.github/workflows` or `.gitlab-ci.yml` for automated tests and releases
-   the `mkdocs.yml` and `docs/` subdirectory to see how the project website works

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

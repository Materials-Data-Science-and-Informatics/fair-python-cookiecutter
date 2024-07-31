# How To Contribute

All kinds of contributions are very welcome!
You can contribute in various ways, e.g. by

-   providing feedback
-   asking questions
-   suggesting ideas
-   implementing features
-   fixing problems
-   improving documentation

To make contributing to open source projects a good experience to everyone involved,
please make sure that you follow our code of conduct when communicating with others.

## Ideas, Questions and Problems

If you have questions or difficulties using this software,
please use the [issue tracker]({{ cookiecutter.project_repo_url }}/issues).

If your topic is not already covered by an existing issue,
please create a new issue using one of the provided issue templates.

If your issue is caused by incomplete, unclear or outdated documentation,
we are also happy to get suggestions on how to improve it.
Outdated or incorrect documentation is a _bug_,
while missing documentation is a _feature request_.

**NOTE:** If you want to report a critical security problem, _do not_ open an issue!
Instead, please create a [private security advisory](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability),
or contact the current package maintainers directly by e-mail.

## Development

This project uses [Poetry](https://python-poetry.org/) for dependency management.

You can run the following lines to check out the project and prepare it for development:

```
git clone {{ cookiecutter.project_repo_url }}
cd {{ cookiecutter.project_slug }}
poetry install --with docs
poetry run poe init-dev
```

Common tasks are accessible via [poe](https://github.com/nat-n/poethepoet):

-   Use `poetry run poe lint` to run linters manually, add `--all-files` to check everything.

-   Use `poetry run poe test` to run tests, add `--cov` to also show test coverage.

-   Use `poetry run poe docs` to generate local documentation

In order to contribute code, please open a pull request.

Before opening the PR, please make sure that your changes

-   are sufficiently covered by meaningful **tests**,
-   are reflected in suitable **documentation** (API docs, guides, etc.), and
-   successfully pass all pre-commit hooks.

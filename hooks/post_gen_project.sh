#!/usr/bin/env bash

# ----
# update lockfile for enabled app demo code deps
# {% if cookiecutter.init_skel.lower() != "-" %}
poetry lock --no-update
# {% endif %}
# remove unneeded demo code
# {% if "cli" not in cookiecutter.init_skel.lower() %}
rm {{ cookiecutter.__project_package }}/cli.py
rm tests/test_cli.py
# {% endif %}
# {% if "api" not in cookiecutter.init_skel.lower() %}
rm {{ cookiecutter.__project_package }}/api.py
rm tests/test_api.py
# {% endif %}
# ----

# finalize repo setup
poetry install --only dev  # to get pre-commit
poetry poe init-dev  # init git repo + register pre-commit
poetry run pipx run reuse download --all  # get license files for REUSE compliance
poetry poe lint update-codemeta --files pyproject.toml  # to create codemeta.json

# create first commit
git checkout -b main  # to make sure the branch is called 'main'
git add .
poetry run git commit -m "first commit - generated project from cookiecutter template"

# add upstream repository
git remote add origin "git@github.com:{{ cookiecutter.__project_gh_name }}.git"

exit 0  # <- uncomment for debugging (keep output dir even in case of errors)

#!/usr/bin/env bash
# Finalization of project template

# create gitlab issue templates by stripping metadata from GH issue templates
for file in .github/ISSUE_TEMPLATE/*; do
    cat $file | awk -v x=0 '
    {
        if ( x > 1 )
            { print }
        if ( $1 ~ /^---/)
            { x++; }
    }' > .gitlab/issue_templates/$(basename $file)
done

# ----
# remove unneeded demo code
# {% if "cli" not in cookiecutter.init_skel.lower() %}
rm src/{{ cookiecutter.__project_package }}/cli.py
rm tests/test_cli.py
# {% endif %}
# {% if "api" not in cookiecutter.init_skel.lower() %}
rm src/{{ cookiecutter.__project_package }}/api.py
rm tests/test_api.py
# {% endif %}
# ----

# finalize repo setup
git init
poetry install
poetry run poe init-dev  # init git repo + register pre-commit
poetry run pip install pipx  # install pipx into venv without adding it as dep
poetry run pipx run reuse download --all  # get license files for REUSE compliance
poetry run poe lint update-codemeta --files pyproject.toml  # to create codemeta.json

# create first commit
git add .
poetry run git commit \
    -m "generated project using fair-python-cookiecutter" \
    -m "https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter"

# make sure that the default branch is called 'main'
git branch -M main

# exit 0  # <- uncomment for debugging (keep output dir even in case of errors)

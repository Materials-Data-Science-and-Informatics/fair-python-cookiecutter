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
# {% if not cookiecutter.init_cli %}
rm src/{{ cookiecutter.project_package }}/cli.py
rm tests/test_cli.py
# {% endif %}
# {% if not cookiecutter.init_api %}
rm src/{{ cookiecutter.project_package }}/api.py
rm tests/test_api.py
# {% endif %}
# ----

# finalize repo setup
git init

# make sure we are not in some venv (or poetry would just use that!)
if pip -V | grep poetry; then
    env=$(pip -V | awk '{print $4}' | sed 's/\/lib\/.*//')
    echo WARNING: deactivating currently active virtual environment "$env"
    source "$env/bin/activate"
    deactivate
fi

poetry install --with docs  # install everything into a new venv
poetry run poe init-dev  # init git repo + register pre-commit
poetry run pip install pipx  # install pipx into venv without adding it as dep
poetry run pipx run reuse download --all  # get license files for REUSE compliance

# copy over the main project license
cp "LICENSES/{{ cookiecutter.project_license }}.txt" LICENSE

# create a minimal codemeta.json based on the CITATION.cff
# (avoiding the buggy codemetapy pyproject.toml parsing)
pipx run cffconvert -i CITATION.cff -f codemeta -o codemeta.json

# create first commit
git add .
poetry run pre-commit run somesy
git add .
poetry run git commit \
    -m "generated project using fair-python-cookiecutter {{ cookiecutter._fpc_version }}" \
    -m "https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter"

# make sure that the default branch is called 'main'
git branch -M main

# sanity-check that main tasks all work
poetry install --with docs 
poetry run poe lint --all-files
poetry run poe test
poetry run poe docs
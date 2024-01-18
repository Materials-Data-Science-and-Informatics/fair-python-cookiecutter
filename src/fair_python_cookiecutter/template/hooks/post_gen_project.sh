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
venv=$(python -c "import sys; print(sys.prefix if sys.base_prefix != sys.prefix else '')")
if [[ -n "$venv" ]]; then
    echo WARNING: deactivating currently active virtual environment "$venv"
    source "$venv/bin/activate"  # make sure we have 'deactivate' available
    deactivate
fi

poetry install --with docs  # install everything into a new venv
poetry run poe init-dev  # init git repo + register pre-commit
poetry run pip install pipx  # install pipx into venv without adding it as dep
poetry run pipx run reuse download --all  # get license files for REUSE compliance
cp "LICENSES/{{ cookiecutter.project_license }}.txt" LICENSE  # copy over the main license

# create CITATION.cff and codemeta.json
git add .
poetry run pre-commit run somesy
git add .

# create first commit
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

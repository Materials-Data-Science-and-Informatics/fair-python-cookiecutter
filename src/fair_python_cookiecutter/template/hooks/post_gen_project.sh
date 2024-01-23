: # Magic to deactivate current Python venv (if one is enabled) in a cross-platform way
: # See https://stackoverflow.com/questions/17510688/single-script-to-run-in-both-windows-batch-and-linux-bash
:<<"::CMDLITERAL"
: ----  code for cmd.exe  ----
ECHO "TODO: cmd.exe code"
: ----------------------------
GOTO :COMMON
::CMDLITERAL
# ---- bash-specific code ----
venv=$(python -c "import sys; print(sys.prefix if sys.base_prefix != sys.prefix else '')")
if [[ -n "$venv" ]]; then
    echo WARNING: deactivating currently active virtual environment "$venv"
    source "$venv/bin/activate"  # make sure we have 'deactivate' available
    deactivate
fi
# ----------------------------
:<<"::CMDLITERAL"
:COMMON
::CMDLITERAL
: #All following code must be hybrid (work for bash and cmd.exe)
: # ------------------------------------------------------------

echo "Initializing the git repository ..."

git init
poetry install --with docs
poetry run poe init-dev

echo "Creating CITATION.cff and codemeta.json using somesy ..."

git add .
poetry run pre-commit run somesy
git add .

echo "Creating first commit ..."

poetry run git commit \
    -m "generated project using fair-python-cookiecutter {{ cookiecutter._fpc_version }}" \
    -m "https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter"

echo "Ensuring that the default branch is called 'main' ..."

git branch -M main

echo "All done! Your project repository is ready :)"


: # TODO: only do following in test mode

: # sanity-check that main tasks all work
: # poetry install --with docs
: # poetry run poe lint --all-files
: # poetry run poe test
: # poetry run poe docs

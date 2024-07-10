: # Magic to deactivate current Python venv (if one is enabled) in a cross-platform way
: # See https://stackoverflow.com/questions/17510688/single-script-to-run-in-both-windows-batch-and-linux-bash
:<<"::CMDLITERAL"
: ----  code for cmd.exe  ----
for /f "delims=" %%a in ('python -c "import sys; print(sys.prefix if sys.base_prefix != sys.prefix else '')"') do set "VENV_PATH=%%a"
IF NOT "%VENV_PATH%" == "" (
    echo INFO: Deactivating currently active virtual environment "%VENV_PATH%"
    REM Assuming the virtual environment needs to be activated first to provide the deactivate script
    call "%VENV_PATH%\Scripts\activate.bat"
    call "%VENV_PATH%\Scripts\deactivate.bat"
)
: ----------------------------
GOTO :COMMON
::CMDLITERAL
# ---- bash-specific code ----
venv=$(python -c "import sys; print(sys.prefix if sys.base_prefix != sys.prefix else '')")
if [[ -n "$venv" ]]; then
    echo INFO: Deactivating currently active virtual environment "$venv"
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

echo "Running all other hooks ..."

poetry run pre-commit run --all
git add .

echo "Creating first commit ..."

poetry run git commit -m "generated project using fair-python-cookiecutter" -m "https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter"

echo "Ensuring that the default branch is called 'main' ..."

git branch -M main

echo "-------->  All done! Your project repository is ready :)  <--------"

: # Magic to deactivate current Python venv (if one is enabled) in a cross-platform way
: # See https://stackoverflow.com/questions/17510688/single-script-to-run-in-both-windows-batch-and-linux-bash
# ---- bash-specific code ----
# venv=$(python -c "import sys; print(sys.prefix if sys.base_prefix != sys.prefix else '')")
if [[ -n "$venv" ]]; then
    echo INFO: Deactivating currently active virtual environment "$venv"
    source "$venv/bin/activate"  # make sure we have 'deactivate' available
    deactivate
fi
# ----------------------------


echo "-------->  All done! Your project repository is ready :)  <--------"


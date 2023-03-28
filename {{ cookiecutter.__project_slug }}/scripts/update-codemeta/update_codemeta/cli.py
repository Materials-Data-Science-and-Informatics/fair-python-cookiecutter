#!/usr/bin/env python3
"""Shallow wrapper around codemetapy to use it with pre-commit."""
# NOTE: if we allow passing args, make sure to either remove -O flag
# or backup the original file if it exists before running.
import subprocess
from pathlib import Path
from typing import List

import rdflib
import rdflib.compare
import typer

app = typer.Typer()


trg_arg = typer.Argument(
    ...,
    file_okay=True,
    dir_okay=False,
)

src_arg = typer.Argument(
    ..., exists=True, file_okay=True, dir_okay=False, readable=True
)


@app.command(
    help="""
Create or update the target codemeta file (first argument)
by running codemetapy with all the other passed arguments.
If the output is the same as before, will keep file unchanged.
"""
)
def update_codemeta(
    target: Path = trg_arg,
    sources: List[str] = src_arg,
):
    old_metadata = rdflib.Graph()
    if target.is_file():
        old_metadata.parse(target)

    ret = subprocess.run(
        ["codemetapy", *sources], shell=True, check=True, capture_output=True
    )
    out = ret.stdout

    # only write result to file if the triples changed
    new_metadata = rdflib.Graph()
    new_metadata.parse(out, format="json-ld")
    if not rdflib.compare.isomorphic(old_metadata, new_metadata):
        typer.echo(f"Project metadata changed, writing {target} ...")
        with open(target, "wb") as f:
            f.write(out)


if __name__ == "__main__":
    app()

#!/usr/bin/env python3
"""Shallow wrapper around codemetapy to use it with pre-commit."""
# NOTE: if we allow passing args, make sure to either remove -O flag
# or backup the original file if it exists before running.
import importlib.resources
import json
import subprocess
from pathlib import Path
from typing import List

import rdflib
import rdflib.compare
import typer

# ----

# expected URLs
codemeta_context = set(
    [
        "https://doi.org/10.5063/schema/codemeta-2.0",
        "https://w3id.org/software-iodata",
        "https://raw.githubusercontent.com/jantman/repostatus.org/"
        "master/badges/latest/ontology.jsonld",
        "https://schema.org",
        "https://w3id.org/software-types",
    ]
)

context_file = "codemeta_context_2023-04-19.json"
with importlib.resources.open_text(__package__, context_file) as c:
    cached_context = json.load(c)


def localize_codemeta_context(json):
    """Prevent rdflib external context resolution by adding it from a file."""
    ctx = set(json.get("@context") or [])
    if not ctx:
        return json  # probably empty or not codemeta, nothing to do
    if ctx != codemeta_context:
        raise RuntimeError(f"Unexpected codemeta context: {json['@context']}")
    ret = dict(json)
    ret.update({"@context": cached_context})
    return ret


# ----


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
        with open(target, "r") as f:
            dat = json.dumps(localize_codemeta_context(json.load(f)))
        old_metadata.parse(data=dat, format="json-ld")

    ret = subprocess.run(["codemetapy", *sources], check=True, capture_output=True)
    out = ret.stdout.decode("utf-8")

    # only write result to file if the triples changed
    new_metadata = rdflib.Graph()
    expanded = json.dumps(localize_codemeta_context(json.loads(out)))
    new_metadata.parse(data=expanded, format="json-ld")

    # print("old")
    # for a, b, c in old_metadata:
    #     print(a, b, c)
    # print("new")
    # for a, b, c in new_metadata:
    #     print(a, b, c)
    # print("same:", rdflib.compare.isomorphic(old_metadata, new_metadata))

    if not rdflib.compare.isomorphic(old_metadata, new_metadata):
        typer.echo(f"Project metadata changed, writing {target} ...")
        with open(target, "w") as f:
            f.write(out)


if __name__ == "__main__":
    app()

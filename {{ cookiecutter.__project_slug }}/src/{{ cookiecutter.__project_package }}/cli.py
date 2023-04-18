"""CLI of {{ cookiecutter.__project_slug }}."""

import typer

from .lib import CalcOperation, calculate

# create subcommand app
say = typer.Typer()

# create main app
app = typer.Typer()
app.add_typer(say, name="say")

# ----


@app.command()
def calc(op: CalcOperation, x: int, y: int):
    result: int = calculate(op, x, y)
    typer.echo(f"Result: {result}")


# ----


@say.command()
def hello(name: str):
    print(f"Hello {name}")


@say.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye {name}. Have a good day.")
    else:
        print(f"Bye {name}!")

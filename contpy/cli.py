"""Console script for contpy."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("contpy")
    click.echo("=" * len("contpy"))
    click.echo("Numerical continuation of dynamical systems")


if __name__ == "__main__":
    main()  # pragma: no cover

#!/usr/bin/python3

### Third-party packages ###
from click import group

### Local modules ###
from niel.commands import create, default, drop, link, unlink


@group
def cli() -> None:
  """niel"""


cli.add_command("create", create)
cli.add_command("default", default)
cli.add_command("drop", drop)
cli.add_command("link", link)
cli.add_command("unlink", unlink)

__all__ = ["cli"]

#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/src/niel/cli.py
# VERSION:     0.1.1
# CREATED:     2024-02-26 23:09
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Third-party packages ###
from click import group, version_option

### Local modules ###
from niel import __version__
from niel.commands import auth, create, default, drop, image, list_menus, set_default, user


@group
@version_option(__version__, message="Niel command-line interface for LINE: %(version)s")
def cli() -> None:
  """niel"""


cli.add_command(auth, "auth")
cli.add_command(create, "create")
cli.add_command(default, "default")
cli.add_command(drop, "drop")
cli.add_command(image, "image")
cli.add_command(list_menus, "list")
cli.add_command(set_default, "set-default")
cli.add_command(user, "user")

if __name__ == "__main__":
  cli()

#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/src/niel/commands/set_default.py
# VERSION:     0.1.0
# CREATED:     2024-05-03 02:03
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************
"""Module defining `set_default` command for `niel` cli"""

### Third-party packages ###
from click import argument, command


@command
@argument("niel-auth-session", envvar="NIEL_AUTH_SESSION")
@argument("rich-menu-id", nargs=1)
def set_default(niel_auth_session: str, rich_menu_id: str) -> None:
  """Set default rich menu identified by `rich_menu_id`

  Args:
      rich_menu_id (str): _description_
  """
  print(niel_auth_session, rich_menu_id)


__all__ = ("set_default",)

#!/usr/bin/env python3.9
# coding:utf-8
# Copyright (C) 2024-2025, All rights reserved.
# FILENAME:    ~~/src/niel/commands/user.py
# VERSION:     0.1.1
# CREATED:     2024-05-07 00:46
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************
"""Module defining `user` command for `niel` cli"""

### Standard packages ###
from re import match

### Third-party packages ###
from click import argument, command
from httpx import Response
from rich import print

### Local modules ###
from niel.client import Line


@command
@argument("id", nargs=1)
@argument("menu-id", nargs=1)
@argument("niel-auth-session", envvar="NIEL_AUTH_SESSION")
def user(id: str, menu_id: str, niel_auth_session: str) -> None:
  """Set rich menu identified by `menu-id` for the user identified by `id`

  Args:
      id (str): TODO: _description_
      menu_id (str): TODO: _description_
  """
  if not match(r"^U[0-9A-Za-z]{32}$", id):
    raise IOError(f"Given parameter '{id}' is malformed; Expected user identifier.")
  if not match(r"^richmenu-[0-9A-Za-z]{32}$", menu_id):
    raise IOError(f"Given parameter '{menu_id}' is malformed; Expected RichMenu identifier.")
  line: Line = Line(channel_token=niel_auth_session)
  response: Response = line.set_user_menu(menu_id, id)
  print(response.status_code == 200)


__all__ = ("user",)

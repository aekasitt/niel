#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/src/niel/commands/drop.py
# VERSION: 	   0.1.0
# CREATED: 	   2024-02-26 23:09
# AUTHOR: 	   Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************
"""Module defining `drop` command for `niel` cli"""

### Standard packages ###
from re import match

### Third-party packages ###
from click import argument, command
from httpx import Response

### Local modules ###
from niel.client import Line


@command
@argument("rich-menu-id", nargs=1)
@argument("niel-auth-session", envvar="NIEL_AUTH_SESSION")
def drop(niel_auth_session: str, rich_menu_id: str):
  """Drop rich menu identified by `rich_menu_id`

  Args:
      rich_menu_id (str): _description_
  """
  if not match(r"^richmenu-[0-9A-Za-z]{32}$", rich_menu_id):
    raise IOError(f"Given parameter '{rich_menu_id}' is malformed; Expected RichMenu identifier.")
  line: Line = Line(channel_token=niel_auth_session)
  response: Response = line.delete_menu(rich_menu_id)
  print(response.status_code == 200)


__all__ = ("drop",)

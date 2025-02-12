#!/usr/bin/env python3.9
# coding:utf-8
# Copyright (C) 2024-2025, All rights reserved.
# FILENAME:    ~~/src/niel/commands/list_menus.py
# VERSION:     0.1.0
# CREATED:     2024-05-29 00:31
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************
"""Module defining `list` command definitions for `niel` cli"""

### Standard packages ###
from re import match
from typing import Dict, List, Literal

### Third-party packages ###
from click import argument, command, option
from httpx import Response
from rich import print

### Local modules ###
from niel.client import Line
from niel.types import RichMenu


@command
@argument("niel-auth-session", envvar="NIEL_AUTH_SESSION")
@option("--ids-only", is_flag=True)
def list_menus(ids_only: bool, niel_auth_session: str) -> None:
  """List RichMenu items created."""
  line: Line = Line(channel_token=niel_auth_session)
  response: Response = line.menus()
  rich_menus: List[Dict[Literal["richMenuId"], str]] = response.json()["richmenus"]
  if ids_only:
    rich_menu_ids: List[str] = [rich_menu["richMenuId"] for rich_menu in rich_menus]
    print(rich_menu_ids)
  else:
    print(rich_menus)


__all__ = ("list_menus",)

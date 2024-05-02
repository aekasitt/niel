#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/src/niel/commands/default.py
# VERSION:     0.1.0
# CREATED:     2024-02-26 23:09
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************
"""Module defining `default` command for `niel` cli"""

### Third-party packages ###
from click import argument, command, option
from httpx import Response

### Local modules ###
from niel.client import Line


@command
@argument("niel-auth-session", envvar="NIEL_AUTH_SESSION")
def default(niel_auth_session: str) -> None:
  """Show default rich menu identifier"""
  line: Line = Line(channel_token=niel_auth_session)
  response: Response = line.default_menu()
  print(response.json()["richMenuId"])


__all__ = ("default",)

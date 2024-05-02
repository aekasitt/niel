#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/src/niel/commands/create.py
# VERSION:     0.1.0
# CREATED:     2024-02-26 23:09
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************
"""Module defining `create` command for `niel` cli"""

### Standard packages ###
from io import BytesIO

### Third-party packages ###
from click import File, argument, command
from httpx import Response
from pydantic import TypeAdapter
from yaml import Loader, load

### Local modules ###
from niel.client import Line
from niel.types import RichMenu


@command
@argument("definitions", type=File("rb"))
@argument("niel_auth_session", envvar="NIEL_AUTH_SESSION")
def create(definitions: BytesIO, niel_auth_session: str) -> None:
  """Create a new rich menu"""
  rich_menu: RichMenu = TypeAdapter(RichMenu).validate_python(load(definitions, Loader=Loader))
  line: Line = Line(channel_token=niel_auth_session)
  response: Response = line.create_menu(rich_menu)
  print(response.json()["richMenuId"])


__all__ = ("create",)

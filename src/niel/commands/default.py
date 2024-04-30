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
from click import argument, command


@command
@argument("rich-menu-id", nargs=1)
def default(rich_menu_id: str) -> None:
  """Show default rich menu identifier"""
  print(rich_menu_id)


__all__ = ("default",)

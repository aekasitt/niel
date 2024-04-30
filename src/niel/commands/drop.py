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

### Third-party packages ###
from click import command, option


@command
@option("--rich-menu-id", help="Identifier for RichMenu object")
def drop(rich_menu_id: str):
  """Drop rich menu identified by `rich_menu_id`

  Args:
      rich_menu_id (str): _description_
  """


__all__ = ("drop",)

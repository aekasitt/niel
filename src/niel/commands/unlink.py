#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/src/niel/commands/unlink.py
# VERSION:     0.1.0
# CREATED:     2024-02-26 23:09
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************
"""Module defining `unlink` command for `niel` cli"""

### Third-party packages ###
from click import command


@command
def unlink() -> None:
  """Unlink RichMenu identified by given rich_menu_id"""


__all__ = ("unlink",)

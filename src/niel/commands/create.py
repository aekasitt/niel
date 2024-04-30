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

### Third-party packages ###
from click import command


@command
def create() -> None:
  """Create a new rich menu"""


__all__ = ["create"]

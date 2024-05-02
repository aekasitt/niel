#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/src/niel/commands/auth.py
# VERSION:     0.1.0
# CREATED:     2024-02-26 23:09
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************
"""Module defining `auth` command for `niel` cli"""

### Standard packages ###
from os import getenv, path
from re import findall
from typing import List

### Third-party packages ###
from click import argument, command


@command
@argument("line-channel-access-token", nargs=1)
def auth(line_channel_access_token: str) -> None:
  """Start an authenticated session"""
  ### Detect shell ###
  shell: str = getenv("SHELL", "/bin/bash")
  rc_path: str = "~/.zshrc" if shell == "/bin/zsh" else "~/.bashrc"
  # TODO: validate parameter
  authenticated: bool = False
  if getenv("NIEL_AUTH_SESSION", None) is not None:
    authenticated = True
  else:
    with open(path.expanduser(rc_path), "r") as rc_readonly:
      found: List[str] = findall("export NIEL_AUTH_SESSION=", rc_readonly.read())
      authenticated = len(found) != 0
  if authenticated:
    print("Already authenticated!")
    return
  if line_channel_access_token is not None:
    with open(path.expanduser(rc_path), "a") as rc_output:
      rc_output.write(f"export NIEL_AUTH_SESSION={ line_channel_access_token }\n")
  print("Success!")


__all__ = ("auth",)

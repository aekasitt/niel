#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/src/niel/commands/image.py
# VERSION:     0.1.0
# CREATED:     2024-05-03 02:25
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************
"""Module defining `image` command for `niel` cli"""

### Standard packages ###
from re import match

### Third-party packages ###
from click import Path, argument, command
from httpx import Response

### Local modules ###
from niel.client import Line


@command
@argument("image-path", nargs=1, type=Path(exists=True))
@argument("menu-id", nargs=1)
@argument("niel-auth-session", envvar="NIEL_AUTH_SESSION")
def image(image_path: str, menu_id: str, niel_auth_session) -> None:
  """Upload an image found by given `image-path` for the RichMenu identified
  by given `menu-id`

  Args:
      image (str): _description_
      menu_id (str): _description_
  """
  if not match(r"^[\-\/0-9A-Z_a-z]+.png$", image_path):
    raise IOError(f"Given parameter '{ image_path }' is malformed; Expected PNG-image file.")
  if not match(r"^richmenu-[0-9A-Za-z]{32}$", menu_id):
    raise IOError(f"Given parameter '{ menu_id }' is malformed; Expected RichMenu identifier.")
  line: Line = Line(channel_token=niel_auth_session)
  with open(image_path, "rb") as image_file:
    response: Response = line.upload(image_file.read(), menu_id)
    print(response.status_code == 200)


__all__ = ("image",)

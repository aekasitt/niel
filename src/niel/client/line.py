#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/src/niel/client/line.py
# VERSION:     0.1.0
# CREATED:     2024-04-30 14:41
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************
"""Module defining `Line` class bundling asynchronous requests for bot management"""

### Standard packages ###
from io import BytesIO
from typing import Dict

### Third-party packages ###
from httpx import Client, Response
from pydantic import BaseModel, StrictStr

### Local modules ###
from niel.types import RichMenu


class Line(BaseModel):
  channel_token: StrictStr
  data_endpoint: StrictStr = "https://api-data.line.me/v2/bot"
  endpoint: StrictStr = "https://api.line.me/v2/bot"

  @property
  def headers(self) -> Dict[str, str]:
    return {"Authorization": f"Bearer {self.channel_token}", "Content-Type": "application/json"}

  def create_menu(self, payload: RichMenu) -> Response:
    """Create a rich menu with defaults and variables included in `payload` object

    Args:
        payload (RichMenu): _description_

    Returns:
        Response: _description_
    """
    with Client(headers=self.headers) as client:
      content: str = payload.model_dump_json(by_alias=True)
      return client.post(f"{self.endpoint}/richmenu", content=content)

  def delete_menu(self, rich_menu_id: str) -> Response:
    """Deletes a richmenu identified by given `rich_menu_id` on LINE Messaging API

    Args:
        rich_menu_id (str): _description_

    Returns:
        dict: _description_
    """
    with Client(headers=self.headers) as client:
      return client.delete(f"{self.endpoint}/richmenu/{rich_menu_id}")

  def default_menu(self) -> Response:
    """Fetches the default `richmenu` from LINE Messaging API

    Returns:
        Response: _description_
    """
    with Client(headers=self.headers) as client:
      return client.get(f"{self.endpoint}/user/all/richmenu")

  def image(self, message_id: str) -> BytesIO:
    """Fetches bytes representing image data from LINE content delivery API

    Args:
        message_id (str): _description_

    Returns:
        BytesIO: _description_
    """
    with Client(headers=self.headers, timeout=10) as client:
      response: Response = client.get(f"{self.data_endpoint}/message/{message_id}/content")
      return BytesIO(response.content)

  def set_default_menu(self, rich_menu_id: str) -> Response:
    """Sets default rich menu for all users to one identified by `rich_menu_id`

    Args:
        rich_menu_id (str): _description_

    Returns:
        Response: _description_
    """
    with Client(headers=self.headers) as client:
      return client.post(f"{self.endpoint}/user/all/richmenu/{rich_menu_id}")

  def set_user_menu(self, rich_menu_id: str, user_id: str) -> Response:
    """Sets user menu to defined `rich_menu_id` using obtained `user_id` from Line Chat Bot interface

    Args:
        rich_menu_id (str): _description_
        user_id (str): _description_

    Returns:
        dict: _description_
    """
    with Client(headers=self.headers) as client:
      return client.post(f"{self.endpoint}/user/{user_id}/richmenu/{rich_menu_id}")

  def upload(self, data: bytes, rich_menu_id: str) -> Response:
    """Upload a PNG-image as a rich menu image identified by `rich_menu_id`

    Args:
        data (BytesIO): _description_
        rich_menu_id (str): _description_

    Returns:
        Response: _description_
    """
    headers: Dict[str, str] = self.headers
    headers["Content-Type"] = "image/png"
    with Client(headers=headers) as client:
      return client.post(f"{self.data_endpoint}/richmenu/{rich_menu_id}/content", content=data)


__all__ = ("Line",)

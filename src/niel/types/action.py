#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/src/niel/types/action.py
# VERSION:     0.1.0
# CREATED:     2024-04-30 13:43
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Local modules ###
from typing import Literal

### Third-party packages ###
from pydantic import BaseModel, Field, StrictStr


class Action(BaseModel):
  action_type: Literal["uri"] = Field("uri", alias="type")
  label: StrictStr
  uri: StrictStr = Field(pattern=r"^https?:\/\/.*$")


__all__ = ("Action",)

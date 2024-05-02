#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/src/niel/types/rich_menu.py
# VERSION:     0.1.0
# CREATED:     2024-04-30 14:41
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Standard packages ###
from typing import List

### Third-party packages ###
from pydantic import BaseModel, Field, StrictBool, StrictStr

### Local modules ###
from niel.types.area import Area
from niel.types.size import Size


class RichMenu(BaseModel):
  areas: List[Area]
  chat_bar_text: StrictStr = Field("Tap to open", alias="chatBarText")
  name: StrictStr
  selected: StrictBool = False
  size: Size = Size()


__all__ = ("RichMenu",)

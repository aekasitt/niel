#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/src/niel/types/area.py
# VERSION:     0.1.0
# CREATED:     2024-04-30 01:22
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Third-party packages ###
from pydantic import BaseModel

### Local modules ###
from niel.types.action import Action
from niel.types.bounds import Bounds


class Area(BaseModel):
  action: Action
  bounds: Bounds


__all__ = ("Area",)

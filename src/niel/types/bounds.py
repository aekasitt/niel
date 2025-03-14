#!/usr/bin/env python3.9
# coding:utf-8
# Copyright (C) 2024-2025, All rights reserved.
# FILENAME:    ~~/src/niel/types/bounds.py
# VERSION:     0.1.1
# CREATED:     2024-04-30 13:43
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Third-party packages ###
from pydantic import BaseModel, NonNegativeInt, PositiveInt


class Bounds(BaseModel):
  height: PositiveInt
  x: NonNegativeInt
  y: NonNegativeInt
  width: PositiveInt


__all__ = ("Bounds",)

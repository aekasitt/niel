#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/src/niel/types/size.py
# VERSION:     0.1.0
# CREATED:     2024-04-30 14:52
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Third-party packages ###
from pydantic import BaseModel, PositiveInt


class Size(BaseModel):
  height: PositiveInt = 843
  width: PositiveInt = 2_500


__all__ = ("Size",)

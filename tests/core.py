#!/usr/bin/env python3.9
# coding:utf-8
# Copyright (C) 2024-2025, All rights reserved.
# FILENAME:    ~~/tests/core.py
# VERSION:     0.1.1
# CREATED:     2025-02-17 12:27
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION: https://www.w3docs.com/snippets/python/what-is-init-py-for.html
#
# HISTORY:
# *************************************************************

### Standard packages ###
from re import sub

### Third-party packages ###
from click.testing import CliRunner

### Local modules ###
from niel.core import niel

def test_interface_without_command() -> None:
    runner: CliRunner = CliRunner()
    result = runner.invoke(niel)
    assert not result.exception
    assert result.output == sub(
      r"\n {6}",
      r"\n",
      """Usage: niel [OPTIONS] COMMAND [ARGS]...

        niel

      Options:
        --version  Show the version and exit.
        --help     Show this message and exit.

      Commands:
        auth         Start an authenticated session
        create       Create a new rich menu
        default      Show default RichMenu identifier
        drop         Drop rich menu identified by `menu-id`
        image        Upload an image found by given `image-path` for the RichMenu...
        list         List RichMenu items created.
        set-default  Set default rich menu identified by `menu-id`
        user         Set rich menu identified by `menu-id` for the user...
      """,
    )

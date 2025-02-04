#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

from fastapi import FastAPI
from pathlib import Path
from typing import Text

from fastapi import FastAPI
from dataclasses import dataclass


def create_app(
    app_name: Text,
)-> FastAPI:
    app = FastAPI(title=app_name)
    return app

@dataclass
class Setting:
    app_name: Text
    version: Text
    updated_at: Text
    exp_folder: Path
    workers: int = 2

def create_settings(
    version: Text,
    exp_folder: Text = "exp",
    workers: int = 2,
)-> Setting:
    """Create setting object for the application.

    Parameters
    ----------
    version : Text
        Path to the version file.
    workers : int, optional
        Number of workers for the application, by default 2

    Returns
    -------
    Setting
        Setting object for the application.

    Examples
    --------
    >>> create_setting("VERSION")
    Setting(app_name='N/A', version='N/A', updated_at='N/A', exp_folder=PosixPath('exp'), workers=2)

    `VERSION` file should be in the following format:
    ```
    APP_NAME    VERSION    UPDATED_AT
    Dementia Detection	0.1.1	2024-01-05
    ```
    """
    try:
        app_name, version, updated_at = Path(version).read_text().split("\n")[0].strip().split('\t')
    except:
        app_name = "N/A"
        version = "N/A"
        updated_at = "N/A"

    return Setting(
        app_name=app_name,
        version=version,
        updated_at=updated_at,
        exp_folder=Path(exp_folder),
        workers=workers,
    )
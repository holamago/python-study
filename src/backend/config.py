#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

from pydantic import BaseModel
from pathlib import Path

# Information of the application
COMPANY = "MAGO"
CONTACT = "galois@holamago.com"
APP_SYMBOL = "scoring"

# Parameters for the application
SERVICE_NAME = "scoring"
TIMEOUT = 60      # 1 minute

try:
    APP_NAME, VERSION, UPDATEDAT = Path("VERSION").read_text().split("\n")[0].strip().split('\t')
except:
    APP_NAME = "Scoring"
    VERSION = "N/A"
    UPDATEDAT = "N/A"

class Settings(BaseModel):
    app_name: str = APP_NAME
    version: str = VERSION
    exp_folder: Path = Path("exp")
    workers: int = 2

settings = Settings()
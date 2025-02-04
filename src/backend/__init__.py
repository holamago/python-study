#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

from pathlib import Path
from .config import settings
from fastapi import FastAPI

def create_app():
    app = FastAPI(title=settings.app_name)
    Path(settings.exp_folder).mkdir(parents=True, exist_ok=True)
    return app

app = create_app()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

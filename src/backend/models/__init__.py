#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

# Information about the language processing model
from ..config import APP_NAME, VERSION, UPDATEDAT
from .request_body import RequestBody

MODEL_INFO = {
    "modelName": APP_NAME,
    "modelVersion": VERSION,
    "createdAt": "2025-02-04",
    "updatedAt": UPDATEDAT,
}

# Import the language processing model
from data import Scoring

engine = Scoring(codebook="../data/emotion_codebook.tsv")


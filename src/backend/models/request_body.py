#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

from pydantic import BaseModel
from typing import Text

class RequestBody(BaseModel):
    lang: Text = "ko"
    min_length: int = 0
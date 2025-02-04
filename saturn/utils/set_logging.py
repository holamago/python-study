#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2022-2023 SATURN
# AUTHORS
# Sukbong Kwon (Galois)

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d: %(name)-20s: %(levelname)s: %(funcName)s(): %(message)s",
    datefmt="%Y-%m-%d %p %I:%M:%S",
)

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)

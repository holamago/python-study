#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2022-2023 SATURN
# AUTHORS
# Sukbong Kwon (Galois)

import logging
import saturn.utils.set_logging
logger = logging.getLogger(__name__.split('.')[-1])

def check_parameters_keys(
    keys: List,
    d: dict
):
    for key in keys:
        if key not in d:
            msg = f"'{key}' key is missed."
            logger.warning(msg)
            return False, msg
    return True, msg

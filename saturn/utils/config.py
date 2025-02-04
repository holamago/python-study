#!/usr/bin/env python
# encoding: utf-8

# The MIT License (MIT)
# Copyright (c) 2022 SATURN

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# AUTHORS
# Sukbong Kwon (Galois)

import os
import json
from typing import List, Dict


def _parse_config(json_data: json, variables: Dict[str, str]) -> None:
    for key, val in json_data.items():
        if type(val) == dict: _parse_config(val, variables)
        elif type(val) == list:
            for v in val:
                if type(v) == dict: _parse_config(v, variables)
        elif type(val) == str:
            json_data[key] = val.format(**variables)


def load_config(fn: str) -> json:
    json_data = json.load(open(fn))
    if 'metadata' in json_data:
        variables = json_data['metadata']['variables']
        for key, val in variables.items():
            variables[key] = val.format(**variables).replace('~', os.path.expanduser('~'))
        _parse_config(json_data, variables)
    return json_data


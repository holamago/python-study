#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

import json
from typing import Dict, Any, Union, Text, List, Optional
from pathlib import Path


def save_json(
    data: Union[Dict, List],
    filename: Union[Text, Path],
    indent: Optional[int] = 4,
)-> Union[Text, Path]:
    """Save data to a json file

    Parameters
    ----------
    data : Union[Dict, List]
        Data to save
    filename : Union[Text, Path]
        Filename to save
    indent : Optional[int], optional
        Indentation level, by default 4

    Returns
    -------
    Union[Text, Path]
        Filename
    """
    data['result_path'] = str(filename)
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    json.dump(data, open(filename, "w"), indent=indent, ensure_ascii=False)
    return filename
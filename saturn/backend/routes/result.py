#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2022- SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

from typing import Text, Dict
from pathlib import Path
from saturn.utils.status_code import (
    MESSAGE_SUCCESS,
    ERROR_PROCESS_FAILED,
)
from .status import Status
from .status import check_status

def get_result(
    id: Text,
    status_path: Path,
    **kwargs,
)-> Dict:
    """Get the result of the batch processing.

    Parameters
    ----------
    id : Text
        The id of the batch processing.
    status_path : Path
        The path of the status file.
    kwargs : Dict
        The parameters for the batch processing.

    Returns
    -------
    Dict
        The result of the batch processing.
    """
    try:
        if not status_path.exists():
            return ERROR_PROCESS_FAILED(
                content={
                    "id": id,
                    "error": "The status file does not exist.",
                }
            ).__dict__

        value, result_path = status_path.read_text().split('\t')
        status = Status(value)

        if status != Status.DONE:
            return check_status(id, status, result_path)

        if not Path(result_path).exists():
            return ERROR_PROCESS_FAILED(
                content={
                    "id": id,
                    "error": "The result file does not exist.",
                }
            ).__dict__

        return MESSAGE_SUCCESS(
            content={
                "id": id,
                "result": result_path,
            }
        ).__dict__

    except Exception as e:
        return ERROR_PROCESS_FAILED(
            content={
                "id": id,
                "error": str(e),
            }
        ).__dict__


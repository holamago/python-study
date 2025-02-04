#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2022- SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

from enum import Enum, auto
from typing import Dict, Text
from pathlib import Path
from saturn.utils.status_code import *

# Define status: the status of processing
class Status(Enum):
    READY    = "READY"
    UPLOADED = "UPLOADED"
    PENDING  = "PENDING"
    RUNNING  = "RUNNING"
    DONE     = "DONE"
    WAITING  = "WAITING"
    FAILED   = "FAILED"


# Check status for the request
def check_status(
    id: Text,
    status: Status,
    detail: Text = "",
)-> Dict:
    """Check status of the request with target status

    Parameters
    ----------
    id : Text
        ID of the request
    status : Status
        Current status of the request
    detail : Text
        Detail message for the status

    Returns
    -------
    Dict
        Response message
    """
    if status == Status.UPLOADED:
        return MESSAGE_UPLOAD_SUCCESS(
            content={"id": id, "detail": f"File {id} is uploaded successfully"}
        ).__dict__

    elif status == Status.RUNNING:
        return MESSAGE_PROCESS_RUNNING_IN_THE_BACKGROUND(
            content={"id": id, "detail": f"File {id} is still being processed"}
        ).__dict__

    elif status == Status.FAILED:
        return ERROR_PROCESS_FAILED(
            content={"id": id, "detail": detail}
        ).__dict__

    elif status == Status.DONE:
        return MESSAGE_PROCESS_DONE(
            content={"id": id, "detail": f"File {id} is processed successfully"}
        ).__dict__

    elif status == Status.WAITING:
        return MESSAGE_PROCESS_WAITING(
            content={"id": id, "detail": f"File {id} is waiting for the process"}
        ).__dict__

    elif status == Status.PENDING:
        return MESSAGE_PROCESS_PENDING(
            content={"id": id, "detail": f"File {id} is pending for the process"}
        ).__dict__

    else:
        return ERROR_INVALID_TASK(
            content={"id": id, "detail": f"File {id} is invalid task, check the status"}
        ).__dict__


def set_status_path(
    id: Text,
    filename: Text,
    our_dir: Path,
)-> Path:
    """Set status path

    Parameters
    ----------
    id : Text
        Content ID required when used as part of multiple tasks
    filename : Text
        Filename

    Returns
    -------
    status_path : Path
        Status file path
    """
    status_path = our_dir / id / f"{id}.status"
    status_path.parent.mkdir(parents=True, exist_ok=True)
    status_path.write_text(f"{Status.READY.value}\t{str(filename)}", encoding="utf-8")

    return status_path
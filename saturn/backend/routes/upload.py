#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2022- SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

import shutil
from fastapi import File, UploadFile
from pathlib import Path
from .status import Status, set_status_path
from typing import Text, Dict, Union, Any, Tuple
from saturn.utils.status_code import ERROR_UPLOAD_FAILED

def upload_file_to_uri(
    id: Text,
    out_dir: Path,
    file: UploadFile = File(...),
)-> Tuple[Path, Path]:
    """Upload a file to the specified directory.

    Parameters
    ----------
    file : UploadFile
        The file to upload. (`UploadFile` is a class from `fastapi`.)

    Returns
    -------
    Tuple[Path, Path]
        The path to the status file and the path of uploaded file.
    """
    status_path = set_status_path(id, file.filename, out_dir) # type: ignore
    file_path = out_dir / id / Path(file.filename) # type: ignore
    upload_file(file, status_path, file_path)
    return status_path, file_path


def upload_file(
    file: Any,
    status_path: Path,
    file_path: Path,
)-> Union[Text, Dict[Text, Any]]:
    """Upload a file to the specified directory.

    Parameters
    ----------
    file : File
        The file to upload. (`File` is a class from `fastapi`.)
    status_path : Path
        The path to the status file.
        It will be updated with the status of the upload.
    file_path : Path
        The path of uploaded file.

    Returns
    -------
    Union[Text, Dict[Text, Any]]
        If the upload fails, return an error message.
        Otherwise, return None.
    """
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        status_path.write_text(f"{Status.UPLOADED.value}\t{str(file_path)}", encoding="utf-8")
    except Exception as e:
        status_path.write_text(f"{Status.FAILED.value}\t{str(e)}", encoding="utf-8")
        return ERROR_UPLOAD_FAILED(
            content={
                "detail": f"Failed to upload {file.filename} with {e}",
            }
        ).__dict__
    finally:
        file.file.close()

    return {}


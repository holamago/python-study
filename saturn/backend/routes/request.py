#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

import json
import uuid
from pathlib import Path
from typing import Dict, Text, Any, Union
from pydantic import BaseModel

from fastapi import (
    BackgroundTasks,
    File,
    UploadFile,
    Depends,
)
from fastapi.responses import JSONResponse

from saturn.backend import (
    set_status_path,
    upload_file,
    run_batch,
    run_batch_uri,
    get_result,
)

from saturn.utils.status_code import (
    MESSAGE_SUCCESS,
    MESSAGE_PROCESS_RUNNING_IN_THE_BACKGROUND,
    ERROR_PROCESS_FAILED,
)

def request_upload(
    engine: Any,
    exp: Union[Text, Path],
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    request_body: BaseModel = Depends(),
)-> JSONResponse:
    """Upload a file to the server and run the background task.

    Parameters
    ----------
    engine : Any
        The engine to run the background task.
    exp : Text
        The path to the experiment folder.
    background_tasks : BackgroundTasks
        The background tasks to run. (FASTAPI class)
    file : UploadFile
        The file to upload. (FASTAPI class)
    request_body : BaseModel
        The request body. (pydantic class)
    """
    # Generate a unique ID for the request
    id = uuid.uuid4().hex

    # Set experiment folder
    exp = Path(exp)

    # Initialize the status file
    status_path = set_status_path(id, str(file.filename), exp)

    # Upload the file
    file_path = exp / id / Path(str(file.filename)).name
    status = upload_file(file, status_path, file_path)
    if  status: JSONResponse(status)

    # Run the background task
    background_tasks.add_task(
        run_batch,
        engine,
        status_path,
        file_path,
        file_path.parent,
        **request_body.dict(),
    )

    # Return the response
    return JSONResponse(
        MESSAGE_PROCESS_RUNNING_IN_THE_BACKGROUND(
            content={
                "id": id,
                "detail": f"File {file.filename} is being processed in the background",
            }
        ).__dict__
    )


def request_run(
    engine: Any,
    model_info: Dict,
    id: Text,
    exp: Union[Text, Path],
    file: UploadFile = File(...),
    request_body: BaseModel = Depends(),
)-> JSONResponse:
    """Upload a file to the server and run task.

    Parameters
    ----------
    engine : Any
        The engine to run task.
    exp : Text
        The path to the experiment folder.
    file : UploadFile
        The file to upload. (FASTAPI class)
    request_body : BaseModel
        The request body. (pydantic class)
    """
    # Generate a unique ID for the request
    if not id: id = uuid.uuid4().hex

    # Set experiment folder
    exp = Path(exp)

    # Initialize the status file
    status_path = set_status_path(id, str(file.filename), exp)

    # Upload the file
    file_path = exp / id / Path(str(file.filename)).name
    status = upload_file(file, status_path, file_path)
    if  status: JSONResponse(status)

    # Run the task
    result = run_batch_uri(
        engine,
        str(file_path),
        id,
        status_path,
        exp / id,
        **request_body.dict(),
    )
    result['model'] = model_info
    return JSONResponse(result)


def request_result(
    id: Text,
    exp: Path,
    model_info: Dict = {},
)-> JSONResponse:
    """Get the result of the request with the given ID.

    Parameters
    ----------
    id : Text
        The ID of the request.
    exp : Path
        The path to the experiment folder.
    model_info : Dict
        The information of the model.

    Returns
    -------
    Dict
        The result of the request.

    Description
    -----------
    Format of status file:
    ```
    Status.DONE    /path/to/result.json
    ```
    """
    # Define the status path
    status_path = exp / id / f"{id}.status"

    # Get the result from the status file
    result = get_result(id, status_path)

    # Check if the result is valid
    if result.get("code", 0) != 700:
        return JSONResponse(result)

    # Return response
    try:
        result_path = result.get('content', {}).get('result', '')
        data = json.load(Path(result_path).open())

        return JSONResponse(
            MESSAGE_SUCCESS(
                model=model_info,
                content={
                    "id": id,
                    "result": data,
                }
            ).__dict__
        )
    except Exception as e:
        return JSONResponse(
            ERROR_PROCESS_FAILED(
                content={
                    "id": id,
                    "error": str(e),
                }
            ).__dict__
        )


def request_uri(
    engine: Any,
    uri: Text,
    id: Text,
    exp: Path,
    model_info: Dict,
    **kwargs: Dict[Text, Any],
)-> JSONResponse:
    """Run a batch processing with the given URI.

    Parameters
    ----------
    uri : Text
        The URI to the input file.
    id : Text
        The ID of the request.
    kwargs : Dict[Text, Any]
        The parameters for the batch processing.

    Returns
    -------
    Dict
        The result of the batch processing.
    """
    # Generate ID (uuid)
    if not id: id = uuid.uuid4().hex

    # Initialize status
    status_path = set_status_path(id, uri, exp)

    # Run batch processing
    result = run_batch_uri(
        engine,
        uri,
        id,
        status_path,
        exp / id,
        **kwargs,
    )
    result['model'] = model_info
    return JSONResponse(result)
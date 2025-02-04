#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2022- SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

# Batch processing in the background

import json
import asyncio
from pathlib import Path
from typing import Dict, Any, Text, Callable, List
from .status import Status, check_status
from saturn.utils.status_code import (
    MESSAGE_SUCCESS,
    ERROR_PROCESS_FAILED,
)


def inference(
    callback: Callable[..., Any],
    file_path: Path,
    out_dir: Path,
    kwargs: Dict[Text, Any],
)-> Any:
    return callback(file_path, out_dir, **kwargs)


async def run_batch(
    callback: Callable[..., Any],
    status_path: Path,
    file_path: Path,
    out_dir: Path,
    **kwargs: Dict[Text, Any],
)-> Text:
    """Run a batch processing in the background.

    Parameters
    ----------
    callback : Callable[..., Any]
        The function to run in the background.
    status_path : Path
        The path to the status file.
        It will be updated with the status of the batch processing.
    file_path : Path
        The path to the input file.
    out_dir : Path
        The path to the output directory.
    kwargs : Dict[Text, Any]
        The parameters for the batch processing.

    Returns
    -------
    Text
        The path to the result file.
    """
    try:
        # Set the status to "running"
        status_path.write_text('\t'.join([Status.RUNNING.value, str(file_path)]), encoding='utf-8')

        # Run the batch processing
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None,
            inference,
            callback,
            file_path,
            out_dir,
            dict(kwargs),
        )

        # Save the result and set the status to "done"
        result_path = status_path.with_suffix(".json")
        json.dump(result, result_path.open('w', encoding='utf-8'), indent=4, ensure_ascii=False)
        status_path.write_text('\t'.join([Status.DONE.value, str(result_path)]), encoding='utf-8')
        return str(result_path)
    except Exception as e:
        # Set the status to "failed"
        status_path.write_text('\t'.join([Status.FAILED.value, str(e)]), encoding='utf-8')
        return ""


def run_batch_uri(
    callback: Callable[..., Any],
    uri: Text,
    id: Text,
    status_path: Path,
    out_dir: Path,
    **kwargs: Dict[Text, Any],
)-> Dict:
    """Run a batch processing with a URI.

    Parameters
    ----------
    callback : Callable[..., Any]
        The function to run in the background.
    uri : Text
        The URI to the input file.
    id : Text
        The unique ID of the request for this process.
    status_path : Path
        The path to the status file.
        It will be updated with the status of the batch processing.
    out_dir : Path
        The path to the output directory.
    kwargs : Dict[Text, Any]
        The parameters for the batch processing.

    Returns
    -------
    Dict
        The result of the batch processing.
    """
    try:
        # Set the status to "running"
        status_path.write_text('\t'.join([Status.RUNNING.value, uri]), encoding="utf-8")

        # Run the batch processing
        result = callback(
            uri,
            out_dir=out_dir,
            **kwargs,
        )
        status_path.write_text('\t'.join([Status.DONE.value, uri]), encoding="utf-8")

        return MESSAGE_SUCCESS(
            content={
                "id": id,
                "result": result,
            }
        ).__dict__

    except Exception as e:
        # Set the status to "failed"
        status_path.write_text('\t'.join([Status.FAILED.value, uri]), encoding="utf-8")

        # Return the error message
        return ERROR_PROCESS_FAILED(
            content={
                "id": id,
                'error': str(e),
            }
        ).__dict__


def run_batch_uris(
    callback: Callable[..., Any],
    uris: List[Text],
    id: Text,
    status_path: Path,
    out_dir: Path,
    **kwargs: Dict[Text, Any],
)-> Dict:
    """Run a batch processing with multiple URIs.

    Parameters
    ----------
    callback : Callable[..., Any]
        The function to run in the background.
    uris : List[Text]
        The URIs to the input files.
    id : Text
        The unique ID of the request for this process.
    status_path : Path
        The path to the status file.
        It will be updated with the status of the batch processing.
    out_dir : Path
        The path to the output directory.
    kwargs : Dict[Text, Any]
        The parameters for the batch processing.

    Returns
    -------
    Dict
        The result of the batch processing.
    """
    try:
        # Set the status to "running"
        status_path.write_text('\t'.join([Status.RUNNING.value, str(uris)]), encoding="utf-8")

        # Run the batch processing
        result = callback(
            uris,
            out_dir=out_dir,
            **kwargs,
        )
        status_path.write_text('\t'.join([Status.DONE.value, str(uris)]), encoding="utf-8")

        return MESSAGE_SUCCESS(
            content={
                "id": id,
                "result": result,
            }
        ).__dict__

    except Exception as e:
        # Set the status to "failed"
        status_path.write_text('\t'.join([Status.FAILED.value, str(uris)]), encoding="utf-8")

        # Return the error message
        return ERROR_PROCESS_FAILED(
            content={
                "id": id,
                'error': str(e),
            }
        ).__dict__
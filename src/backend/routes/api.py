#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

import uuid
from pathlib import Path
from typing import Text, Dict

from fastapi import (
    APIRouter,
    Depends,
    Body,
)
from fastapi.responses import JSONResponse

from .. import config
from ..models import engine
from saturn.utils.status_code import (
    MESSAGE_SUCCESS,
    ERROR_PROCESS_FAILED,
    ERROR_FILE_NOT_FOUND,
    ERROR_TASK_NOT_SUPPORTED,
    ERROR_INPUT_IS_EMPTY,
)

EXP_FOLDER = config.settings.exp_folder / config.SERVICE_NAME
EXP_FOLDER.mkdir(parents=True, exist_ok=True)


# Define router
router = APIRouter(
    prefix = f"/{config.APP_SYMBOL}",
    tags=[config.APP_SYMBOL],
    responses={404: {"description": "Not found"}},
)

############################################
# API Endpoints
############################################

@router.get("/", operation_id="overview_endpoint")
async def overview():
    return """문장의 점수를 계산합니다.
    단어마다 점수를 기록한 데이터로부터 문장의 점수를 계산합니다.
    주어진 단어와 데이터베이스에 있는 단어의 거리는 Edit Distance로 계산합니다.
    """

@router.post("/run", operation_id="run_endpoint")
async def run(
    request: str = Body(..., media_type='text/plain'),
    id: Text = "",
)-> JSONResponse:
    """Run the language processing application
    """
    # Generate a content ID (uuid)
    if not id:  id = uuid.uuid4().hex

    # Check if the input is empty
    if not request:
        return JSONResponse(ERROR_INPUT_IS_EMPTY(
                content={"id": id}
            ).__dict__)

    result = engine(request)

    try:
        return JSONResponse(MESSAGE_SUCCESS(
            content={
                "id": id,
                "result": result,
            }
        ).__dict__)

    except Exception as e:
        return JSONResponse(ERROR_PROCESS_FAILED(
            content={
                'error': str(e),
            }
        ).__dict__)


#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2022 SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

from typing import Dict, Text
from dataclasses import dataclass


#################################################
############## MESSSAGE CODES ###################
#################################################
@dataclass
class MESSAGE_SUCCESS:
    code: int = 700
    message: Text = "Success"
    model: Dict = None
    content: Dict = None


@dataclass
class MESSAGE_UPLOAD_SUCCESS:
    code: int = 701
    message: Text = "Upload success"
    content: Dict = None

@dataclass
class MESSAGE_PROCESS_RUNNING:
    code: int = 702
    message: Text = "Process is running"
    content: Dict = None

@dataclass
class MESSAGE_PROCESS_RUNNING_IN_THE_BACKGROUND:
    code: int = 703
    message: Text = "Process is running in the background"
    content: Dict = None

@dataclass
class MESSAGE_PROCESS_DONE:
    code: int = 704
    message: Text = "Process is done"
    content: Dict = None

@dataclass
class MESSAGE_PROCESS_NOT_YET_RUNNING:
    code: int = 705
    message: Text = "Process is not yet running"
    content: Dict = None

@dataclass
class MESSAGE_PROCESS_PENDING:
    code: int = 706
    message: Text = "Process is pending"
    content: Dict = None

@dataclass
class MESSAGE_PROCESS_WAITING:
    code: int = 707
    message: Text = "Process is waiting"
    content: Dict = None


#################################################
############## MESSSAGE ERROR ###################
#################################################

# General errors
@dataclass
class ERROR_UNKNOWN:
    code: int = 500
    message: Text = "Unknown error"
    content: Dict = None

@dataclass
class ERROR_PROCESS_FAILED:
    code: int = 501
    message: Text = "Process failed"
    content: Dict = None

@dataclass
class ERROR_UPLOAD_FAILED:
    code: int = 502
    message: Text = "Upload failed"
    content: Dict = None

@dataclass
class ERROR_SERVER_IS_BUSY:
    code: int = 503
    message: Text = "Process is already running"
    content: Dict = None

# Invalid request errors
@dataclass
class ERROR_INVALID_ID:
    code: int = 510
    message: Text = "Invalid ID"
    content: Dict = None


@dataclass
class ERROR_INVALID_TASK:
    code: int = 511
    message: Text = "Invalid task"
    content: Dict = None


@dataclass
class ERROR_INVALID_KEY:
    code: int = 512
    message: Text = "Invalid key"
    content: Dict = None


@dataclass
class ERROR_FILE_NOT_FOUND:
    code: int = 513
    message: Text = "File not found"
    content: Dict = None

# Audio related errors

@dataclass
class ERROR_INVALID_AUDIO:
    code: int = 520
    message: Text = "Invalid audio"

# Task, request, and model related errors
@dataclass
class ERROR_TASK_NOT_SUPPORTED:
    code: int = 521
    message: Text = "Task not supported"
    content: Dict = None

@dataclass
class ERROR_INPUT_IS_EMPTY:
    code: int = 522
    message: Text = "Input is empty"
    content: Dict = None
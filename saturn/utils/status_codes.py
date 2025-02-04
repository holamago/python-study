#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2022 SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

from typing import Dict

def generate_message(
    msg: Dict,
    contents: Dict
)-> Dict:
    """
    Generate message

    Parameters
    ----------
    msg : Dict
        Error message
    contents : Dict
        Contents of error message

    Returns
    -------
    Dict
        Error message
    """
    msg["contents"] = contents
    return msg


# ERROR CODES
ERR_UNKNOWN_CODE = 599
ERR_UPLOADING_FAILED_CODE = 500
ERR_REQUEST_NOT_FOUND_CODE = 501
ERR_SERVER_IS_BUSY_CODE = 502
ERR_PROCESS_FAILED_CODE = 503
ERR_INVALID_PARAMTER_CODE = 504
ERR_INVALID_ID_CODE = 505
ERR_INVALID_TASK_CODE = 506
ERR_INVALID_KEY_CODE = 507
ERR_INVALID_VALUE_CODE = 508
ERR_INVALID_PATH_CODE = 509
ERR_INVALID_FILE_CODE = 510
ERR_FILE_NOT_FOUND_CODE = 511
ERR_MEDIA_NOT_FOUND_CODE = 512
ERR_ADUIO_NOT_FOUND_CODE = 513
ERR_SPEECH_NOT_FOUND_CODE = 514
ERR_TEXT_NOT_FOUND_CODE = 515
ERR_MODEL_NOT_FOUND_CODE = 516
ERR_MODEL_NOT_LOADED_CODE = 517
ERR_LANGUAGE_NOT_SUPPORTED_CODE = 520

ERR_MEDIA_FORMAT_NOT_SUPPORTED_CODE = 530
ERR_VIDEO_FORMAT_NOT_SUPPORTED_CODE = 531
ERR_AUDIO_FORMAT_NOT_SUPPORTED_CODE = 532
ERR_SPEECH_FORMAT_NOT_SUPPORTED_CODE = 533
ERR_TOO_LONG_CODE = 535
ERR_TOO_SHORT_CODE = 536

ERR_LYRICS_NOT_FOUND_CODE = 540
ERR_SCRIPT_NOT_FOUND_CODE = 541
ERR_RESULT_NOT_FOUND_CODE = 542

class ERR_UNKNOWN(Exception):
    def __init__(self, contents=None):
        self.code = ERR_UNKNOWN_CODE
        self.message = "Unknown error."
        self.contents = contents

class ERR_UPLOADING_FAILED(Exception):
    def __init__(self, contents=None):
        self.code = ERR_UPLOADING_FAILED_CODE
        self.message = "Uploading failed."
        self.contents = contents

class ERR_REQUEST_NOT_FOUND(Exception):
    def __init__(self, contents=None):
        self.code = ERR_REQUEST_NOT_FOUND_CODE
        self.message = "Request ID is not found, check it."
        self.contents = contents

class ERR_SERVER_IS_BUSY(Exception):
    def __init__(self, contents=None):
        self.code = ERR_SERVER_IS_BUSY_CODE
        self.message = "Server is busy, try it later."
        self.contents = contents

class ERR_PROCESS_FAILED(Exception):
    def __init__(self, contents=None):
        self.code = ERR_PROCESS_FAILED_CODE
        self.message = "Process failed, try again later."
        self.contents = contents

class ERR_INVALID_PARAMTER(Exception):
    def __init__(self, contents=None):
        self.code = ERR_INVALID_PARAMTER_CODE
        self.message = "Invalid parameter, check it."
        self.contents = contents

class ERR_INVALID_ID(Exception):
    def __init__(self, contents=None):
        self.code = ERR_INVALID_ID_CODE
        self.message = "Invalid ID, check it."
        self.contents = contents

class ERR_INVALID_TASK(Exception):
    def __init__(self, contents=None):
        self.code: int = ERR_INVALID_TASK_CODE
        self.message: str = "Invalid task, check it."
        self.contents = contents

class ERR_INVALID_KEY(Exception):
    def __init__(self, key="", contents=None):
        self.code = ERR_INVALID_KEY_CODE
        self.message = f"Invalid key '{key}', check it."
        self.contents = contents


class ERR_INVALID_VALUE(Exception):
    def __init__(self, key="", value="", contents=None):
        self.code = ERR_INVALID_VALUE_CODE
        self.message = f"Invalid value '{value}' of the key '{key}', check it."
        self.contents = contents

class ERR_INVALID_PATH(Exception):
    def __init__(self, contents=None):
        self.code = ERR_INVALID_PATH_CODE
        self.message = "Invalid path, check it."
        self.contents = contents

class ERR_INVALID_FILE(Exception):
    def __init__(self, contents=None):
        self.code = ERR_INVALID_FILE_CODE
        self.message = "Invalid file, check it."
        self.contents = contents

class ERR_FILE_NOT_FOUND(Exception):
    def __init__(self, contents=None):
        self.code = ERR_FILE_NOT_FOUND_CODE
        self.message = "File not found, check it."
        self.contents = contents

class ERR_MEDIA_NOT_FOUND(Exception):
    def __init__(self, contents=None):
        self.code = ERR_MEDIA_NOT_FOUND_CODE
        self.message = "Media not found, check it."
        self.contents = contents

class ERR_AUDIO_NOT_FOUND(Exception):
    def __init__(self, contents=None):
        self.code = ERR_ADUIO_NOT_FOUND_CODE
        self.message = "Audio not found, check it."
        self.contents = contents

class ERR_SPEECH_NOT_FOUND(Exception):
    def __init__(self, contents=None):
        self.code = ERR_SPEECH_NOT_FOUND_CODE
        self.message = "Speech not found, check it."
        self.contents = contents

class ERR_TEXT_NOT_FOUND(Exception):
    def __init__(self, contents=None):
        self.code = ERR_TEXT_NOT_FOUND_CODE
        self.message = "Text not found, check it."
        self.contents = contents

class ERR_MODEL_NOT_FOUND(Exception):
    def __init__(self, contents=None):
        self.code = ERR_MODEL_NOT_FOUND_CODE
        self.message = "Model not found, check it."
        self.contents = contents

class ERR_MODEL_NOT_LOADED(Exception):
    def __init__(self, contents=None):
        self.code = ERR_MODEL_NOT_LOADED_CODE
        self.message = "Model not loaded, check it."
        self.contents = contents

class ERR_LANGUAGE_NOT_SUPPORTED(Exception):
    def __init__(self, contents=None):
        self.code = ERR_LANGUAGE_NOT_SUPPORTED_CODE
        self.message = "Language is not supported, check it."
        self.contents = contents

class ERR_MEDIA_FORMAT_NOT_SUPPORTED(Exception):
    def __init__(self, contents=None):
        self.code = ERR_MEDIA_FORMAT_NOT_SUPPORTED_CODE
        self.message = "Media format is not supported, check it."
        self.contents = contents

class ERR_VIDEO_FORMAT_NOT_SUPPORTED(Exception):
    def __init__(self, contents=None):
        self.code = ERR_VIDEO_FORMAT_NOT_SUPPORTED_CODE
        self.message = "Video format is not supported, check it."
        self.contents = contents

class ERR_AUDIO_FORMAT_NOT_SUPPORTED(Exception):
    def __init__(self, contents=None):
        self.code = ERR_AUDIO_FORMAT_NOT_SUPPORTED_CODE
        self.message = "Audio format is not supported, check it."
        self.contents = contents

class ERR_SPEECH_FORMAT_NOT_SUPPORTED(Exception):
    def __init__(self, contents=None):
        self.code = ERR_SPEECH_FORMAT_NOT_SUPPORTED_CODE
        self.message = "Speech format is not supported, check it."
        self.contents = contents

class ERR_MEDIA_IS_TOO_LONG(Exception):
    def __init__(self, contents=None):
        self.code = ERR_TOO_LONG_CODE
        self.message = "Media is too long, check it."
        self.contents = contents

class ERR_MEDIA_IS_TOO_SHORT(Exception):
    def __init__(self, contents=None):
        self.code = ERR_TOO_SHORT_CODE
        self.message = "Media is too short, check it."
        self.contents = contents


class ERR_LYRICS_NOT_FOUND(Exception):
    def __init__(self, contents=None):
        self.code = ERR_LYRICS_NOT_FOUND_CODE
        self.message = "Lyrics file is not exist, check it."
        self.contents = contents


class ERR_SCRIPT_NOT_FOUND(Exception):
    def __init__(self, contents=None):
        self.code = ERR_SCRIPT_NOT_FOUND_CODE
        self.message = "Script file is not exist, check it."
        self.contents = contents


class ERR_RESULT_NOT_FOUND(Exception):
    def __init__(self, contents=None):
        self.code = ERR_RESULT_NOT_FOUND_CODE
        self.message = "Result file is not exist, check it."
        self.contents = contents


# WARNING CODES
WARN_SPEECH_NOT_FOUND_CODE = 600
WARN_SHORT_AUDIO_CODE = 601
WARN_SPEECH_IS_ODD_CODE = 602
WARN_NOISE_HIGH_CODE = 603
WARN_VOICE_LOW_CODE = 604
WARN_SOUND_LOW_CODE = 605
WARN_SPEECH_NOT_RECOGNIZED_CODE = 606

WARN_SPEECH_NOT_FOUND = {
    "code": WARN_SPEECH_NOT_FOUND_CODE,
    "message": "Speech not found, check it."
}

WARN_SHORT_AUDIO = {
    "code": WARN_SHORT_AUDIO_CODE,
    "message": "Audio is too short, check it.",
}

WARN_SPEECH_IS_ODD = {
    "code": WARN_SPEECH_IS_ODD_CODE,
    "message": "Speech is odd, check it.",
}

WARN_NOISE_HIGH = {
    "code": WARN_NOISE_HIGH_CODE,
    "message": "Noise is high, check it.",
}

WARN_VOICE_LOW = {
    "code": WARN_VOICE_LOW_CODE,
    "message": "Voice is low, check it.",
}

WARN_SOUND_LOW = {
    "code": WARN_SOUND_LOW_CODE,
    "message": "Sound is low, check it.",
}

WARN_SPEECH_NOT_RECOGNIZED = {
    "code": WARN_SPEECH_NOT_RECOGNIZED_CODE,
    "message": "Speech not recognized, check it.",
}


# MESSSAGES CODES
MSG_SUCCESS_CODE = 700

MSG_SUCCESS = {
    "code": MSG_SUCCESS_CODE,
    "message": "Success",
}

MSG_UPLOAD_SUCCESS_CODE = 701
MSG_PROCESS_ALREADY_RUNNING_CODE = 710
MSG_PROCESS_DONE_CODE = 711
MSG_PROCESS_RUNNING_IN_THE_BACKGROUND_CODE = 712
MSG_PROCESS_NOT_YET_RUNNING_CODE = 713
MSG_PROCESS_PENDING_CODE = 714
MSG_PROCESS_WAITING_CODE = 715

MSG_UPLOAD_SUCCESS = {
    "code": MSG_UPLOAD_SUCCESS_CODE,
    "message": "Upload success",
}


MSG_PROCESS_ALREADY_RUNNING = {
    "code": MSG_PROCESS_ALREADY_RUNNING_CODE,
    "message": "Process is already running",
}

MSG_PROCESS_DONE = {
    "code": MSG_PROCESS_DONE_CODE,
    "message": "Process is done",
}

MSG_PROCESS_RUNNING_IN_THE_BACKGROUND = {
    "code": MSG_PROCESS_RUNNING_IN_THE_BACKGROUND_CODE,
    "message": "Process is running in the background",
}

MSG_PROCESS_NOT_YET_RUNNING = {
    "code": MSG_PROCESS_NOT_YET_RUNNING_CODE,
    "message": "Process is not yet running",
}

MSG_PROCESS_PENDING = {
    "code": MSG_PROCESS_PENDING_CODE,
    "message": "Process is pending",
}

MSG_PROCESS_WAITING = {
    "code": MSG_PROCESS_WAITING_CODE,
    "message": "Process is waiting",
}

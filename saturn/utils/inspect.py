#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

import torchaudio
from typing import Text

def get_audio_info(
    audio_path: Text,
):
    """Get audio information

    Parameters
    ----------
    audio_path : str
        Audio path

    Returns
    -------
    dict
        Audio information
    """
    # Get duration, samplerate, and channels
    waveform, sample_rate = torchaudio.load(audio_path)
    duration = waveform.size(1) / sample_rate
    channels = waveform.size(0)

    return {
        "duration": round(duration, 3),
        "samplerate": sample_rate,
        "channels": channels,
    }
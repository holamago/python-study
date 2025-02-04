#!/usr/bin/env python
# encoding: utf-8

# The MIT License (MIT)
# Copyright (c) 2022 SATURN

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# AUTHORS
# Sukbong Kwon (Galois)


from datetime import timedelta, datetime

def seconds2time_lrc(
    seconds: float,
) -> str:
    negative = seconds < 0
    seconds = abs(seconds)
    td = timedelta(seconds=seconds)
    seconds = td.seconds + 86400 * td.days
    microseconds = td.microseconds
    minutes, seconds = divmod(seconds, 60)
    return '%02d:%02d.%02d' % (
        '-' if negative else minutes,
        seconds, round(microseconds / 10000))

    
def time2seconds_lrc(
    time: str,
):
    date_time = datetime.strptime(time,'%M:%S.%f')
    a_timedelta = date_time - datetime(1900, 1, 1)
    seconds = a_timedelta.total_seconds()
    return seconds


def seconds2time_srt(
    seconds: float,
) -> str:
    negative = seconds < 0
    seconds = abs(seconds)
    td = timedelta(seconds=seconds)
    seconds = td.seconds + 86400 * td.days
    microseconds = td.microseconds
    hours, residual = divmod(seconds, 3600)
    minutes, seconds = divmod(residual, 60)
    return '%02d:%02d:%02d,%03d' % (
        '-' if negative else hours, minutes,
        seconds, round(microseconds / 1000))


def time2seconds_srt(
    time: str,
):
    date_time = datetime.strptime(time,'%H:%M:%S,%f')
    a_timedelta = date_time - datetime(1900, 1, 1)
    seconds = a_timedelta.total_seconds()
    return seconds


def seconds2time_audio(
    seconds: float,
) -> str:
    negative = seconds < 0
    seconds = abs(seconds)
    td = timedelta(seconds=seconds)
    seconds = td.seconds + 86400 * td.days
    microseconds = td.microseconds
    hours, residual = divmod(seconds, 3600)
    minutes, seconds = divmod(residual, 60)
    return '%02d:%02d:%02d.%02d' % (
        '-' if negative else hours, minutes,
        seconds, round(microseconds / 10000))


def time2seconds_audio(
    time: str,
):
    date_time = datetime.strptime(time,'%H:%M:%S.%f')
    a_timedelta = date_time - datetime(1900, 1, 1)
    seconds = a_timedelta.total_seconds()
    return seconds

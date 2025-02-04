#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2022 SATURN
# AUTHORS
# Sukbong Kwon (Galois)

from functools import reduce
from typing import Text
from argparse import Namespace
from type_docopt import docopt

def args2params(args):
    repls =  {'--' : '', '<': '', '>' : '', '-': '_'}
    params = {}
    for key, val in args.items():
        params[reduce(lambda a, kv: a.replace(*kv), repls.items(), key)] = val
    return params

def arg2kwargs(args):
    return reduce(lambda a, kv: a.update(kv) or a, args2params(args).items(), {})


def get_params(
    __doc__,
    version_path: Text = "",
)-> Namespace:
    if version_path:
        version = open(version_path).read().strip('\n')[0]
    else:
        version = 'not defined'
    args = docopt(__doc__, version=f"{version}")
    return Namespace(**args2params(args))
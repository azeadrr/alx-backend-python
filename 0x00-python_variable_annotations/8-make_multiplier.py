#!/usr/bin/env python3
"""functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function make_multiplier
    takes a float multiplier as argument
    """
    return lambda x: x * multiplier

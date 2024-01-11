#!/usr/bin/env python3
"""
Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """function sum_list
    takes a list input_list of floats
    returns their sum as a float"""
    return float(sum(input_list))

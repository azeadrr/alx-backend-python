#!/usr/bin/env python3
"""mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """function sum_mixed_list
    takes a list mxd_lst
    of integers and floats
    returns their sum as a float
    """
    return float(sum(mxd_list))

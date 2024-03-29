#!/usr/bin/env python3
"""involved type"""
from typing import Any, Mapping, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Given the parameters and the return values
    """
    if key in dct:
        return dct[key]
    else:
        return default

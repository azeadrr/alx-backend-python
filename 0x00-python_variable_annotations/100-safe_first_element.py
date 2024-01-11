#!/usr/bin/env python3
"""first element of a sequence"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """take lst as argument
    return first element of the list
    """
    if lst:
        return lst[0]
    else:
        return None

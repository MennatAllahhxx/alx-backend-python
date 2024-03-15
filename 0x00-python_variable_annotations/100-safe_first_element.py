#!/usr/bin/env python3
"""
Module contains safe_first_element fun
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """AI is creating summary for safe_first_element

    Args:
        lst (Sequence[Any]): a sequence of any type of elements

    Returns:
        Union[Any, None]: sequence's 1st element if exists
    """
    if lst:
        return lst[0]
    else:
        return None

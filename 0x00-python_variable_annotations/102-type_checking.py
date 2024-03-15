#!/usr/bin/env python3
"""
Module contains zoom_array fun
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """AI is creating summary for zoom_array

    Args:
        lst (Tuple): input
        factor (int, optional): range. Defaults to 2.

    Returns:
        List: a list
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

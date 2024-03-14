#!/usr/bin/env python3
"""
Module contains sum_mixed_list fun
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """AI is creating summary for sum_list

    Args:
        mxd_lst (List[Union[int, float]]): a list of floats and integers

    Returns:
        float:  their sum as a float
    """
    total: float = 0.0
    for i in mxd_lst:
        total += i
    return total

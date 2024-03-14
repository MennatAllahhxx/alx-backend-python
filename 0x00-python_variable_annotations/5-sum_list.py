#!/usr/bin/env python3
"""
Module contains sum_list fun
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """AI is creating summary for sum_list

    Args:
        input_list (List[float]): a list of floats

    Returns:
        float:  their sum as a float
    """
    total: float = 0.0
    for i in input_list:
        total += i
    return total

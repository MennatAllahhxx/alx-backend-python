#!/usr/bin/env python3
"""
Module contains to_kv fun
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """AI is creating summary for to_kv

    Args:
        k (str): 1st arg in tuple, string
        v (Union[int, float]): 2nd arg in tuple, float or integer

    Returns:
        Tuple[str, Union[int, float]]: The first element of the tuple
        is the string k. The second element is the square of the int/float v
    """
    return (k, v*v)

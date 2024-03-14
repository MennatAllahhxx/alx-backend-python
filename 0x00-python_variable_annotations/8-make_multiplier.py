#!/usr/bin/env python3
"""
Module contains make_multiplier fun
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """AI is creating summary for make_multiplier

    Args:
        multiplier (float): a factor to mult the number

    Returns:
        Callable[[float], float]: a fun that multi factor by number
    """

    def mult(num: float) -> float:
        """AI is creating summary for mult

        Args:
            num (float): number to be muliplied

        Returns:
            float: multiplication of factor by number
        """
        return multiplier * num
    return mult

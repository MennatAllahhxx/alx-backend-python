#!/usr/bin/env python3
"""
Module contains element_length fun
"""
from typing import Sequence, Tuple, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """AI is creating summary for element_length

    Args:
        lst (Iterable[Sequence]): iterable sequence

    Returns:
        List[Tuple[Sequence, int]]: a list of tuble of sequence and its length
    """
    return [(i, len(i)) for i in lst]

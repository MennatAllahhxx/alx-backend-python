#!/usr/bin/env python3
"""
Module contains task_wait_n fun
"""

from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """AI is creating summary for task_wait_n

    Args:
        n (int): number of times to perform wait_random.
        max_delay (int): max delay to be sent to wait_random.

    Returns:
        List[float]: a sorted list of the returning values from wait_random.
    """
    lst: List[float] = []

    for _ in range(n):
        lst.append(await task_wait_random(max_delay))

    return sorted(lst)

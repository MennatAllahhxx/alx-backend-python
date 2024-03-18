#!/usr/bin/env python3
"""
Module contains task_wait_random fun
"""

from asyncio import Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """AI is creating summary for task_wait_random

    Args:
        max_delay (int): max delay to be sent to wait_random.

    Returns:
        Task: wait_random task returns after running
    """
    return Task(wait_random(max_delay))

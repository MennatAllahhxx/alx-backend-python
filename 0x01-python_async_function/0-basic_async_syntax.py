#!/usr/bin/env python3
"""
Module contains wait_random coroutine
"""

import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """AI is creating summary for wait_random

    Args:
        max_delay (int, optional): maximum delay for the coroutine.
        Defaults to 10.

    Returns:
        float: the delay of the function resulting from random function
    """
    random_delay = uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay

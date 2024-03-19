#!/usr/bin/env python3
"""
Module contains measure_runtime coroutine
"""

from time import time
from asyncio import gather

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """AI is creating summary for measure_runtime

    Returns:
        float: total runtime.
    """
    start_time = time()

    await gather(*[async_comprehension() for _ in range(4)])

    end_time = time()

    return (end_time - start_time)

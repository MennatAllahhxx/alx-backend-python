#!/usr/bin/env python3
"""
Module contains async_comprehension coroutine
"""

import asyncio
from random import uniform
from typing import Generator, List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """AI is creating summary for async_comprehension

    Returns:
        List[float]: 10 random numbers that where collected using
        async_generator.
    """
    lst: List[float] = [j async for j in async_generator()]
    return lst

#!/usr/bin/env python3
"""
Module contains measure_time fun
"""

import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """AI is creating summary for measure_time

    Args:
        n (int): number of times to be sent to wait_n to perform wait_random.
        max_delay (int): max delay to be sent to wait_n.

    Returns:
        float: average time taken by 1 wait_random
    """
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time()
    avg_time = (end_time - start_time)/n
    return avg_time

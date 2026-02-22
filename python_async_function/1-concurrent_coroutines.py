#!/usr/bin/env python3
"""
This module provides a function to execute
multiple coroutines at the same time.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Returns the list of all the delays (float values)
    in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Use asyncio.as_completed to get results as they finish
    # (this naturally sorts them by completion time/delay)
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays

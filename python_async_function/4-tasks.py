#!/usr/bin/env python3
"""
This module provides a function  that calls another module.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function implements code from wait_n
    and alter it into a new one.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Use asyncio.as_completed to get results as they finish
    # (this naturally sorts them by completion time/delay)
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays

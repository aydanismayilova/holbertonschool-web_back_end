#!/usr/bin/env python3
"""
This module provides an asynchronous function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function takes an integer as an argument
    waits for a random delay and returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

#!/usr/bin/env python3
"""
This module provides a function to return a Task object.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function takes an integer and returns as asyncio.Task.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task

#!/usr/bin/env python3
"""
This module provides type-annotated function that
takes different arguments and returns tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string as first argument and an int
    or a float as second and returns as a tuple with mixed data types.
    """
    return (k, v**2)

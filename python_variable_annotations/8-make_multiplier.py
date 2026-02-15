#!/usr/bin/env python3
"""
This module provides a function to multiply a float.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float multiplier as an argument and
    returns the multiplied float by that multiplier.
    """
    def multiplier_func(n: float) -> float:
        """
        Multiplies a float by the multiplier.
        """
        return n * multiplier

    return multiplier_func

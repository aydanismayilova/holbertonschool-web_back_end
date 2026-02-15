#!/usr/bin/env python3
"""
This module provides type-annotated function fo addition.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list of floats as argument
    and returns their sum as float.
    """
    return sum(input_list)

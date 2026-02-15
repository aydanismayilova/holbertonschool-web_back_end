#!/usr/bin/env python3
"""
This module provides type-annotated function
to sum lists with different data types.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function takes a mixed list of integers and floats
    and returns their sum as float.
    """
    return sum(mxd_lst)

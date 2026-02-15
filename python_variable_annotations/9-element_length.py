#!/usr/bin/env python3
"""
This module provides duck type of an iterable object.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each element in the given iterable of sequences.
    Returns a list of tuples, each containing an element and its length.
    """
    return [(i, len(i)) for i in lst]

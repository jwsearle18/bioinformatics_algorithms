"""
This file contains an implementation of the Burrows-Wheeler transform.
"""

import sys
from typing import List, Dict, Iterable, Tuple

def burrows_wheeler_transform(text: str) -> str:
    """
    Computes the Burrows-Wheeler transform of a string.

    Args:
        text: The string to transform.

    Returns:
        The Burrows-Wheeler transform of the string.
    """
    suffixes = []
    transform = ""
    for i in range(len(text)):
        suffixes.append(text[i:] + text[:i])
    suffixes = sorted(suffixes)
    for suffix in suffixes:
        transform += suffix[-1]
    return transform
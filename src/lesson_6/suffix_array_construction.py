"""
This file contains an implementation of the suffix array construction algorithm.
"""

import sys
from typing import List, Dict, Iterable, Tuple

def suffix_array(text: str) -> List[int]:
    """
    Constructs the suffix array of a string.

    Args:
        text: The string to construct the suffix array from.

    Returns:
        The suffix array of the string.
    """
    suffixes = []
    for i in range(len(text)):
        suffixes.append([text[i:], i])
    suffixes = sorted(suffixes)
    formated = []
    for suffix in suffixes:
        formated.append(suffix[1])
    return formated
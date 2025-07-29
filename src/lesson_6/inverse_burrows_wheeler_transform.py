"""
This file contains an implementation of the inverse Burrows-Wheeler transform.
"""

import sys
from typing import List, Dict, Iterable, Tuple

def create_occurance_list(text: str) -> List[Tuple[str, int]]:
    """
    Creates a list of occurrences of each character in a string.

    Args:
        text: The string to process.

    Returns:
        A list of tuples, where each tuple contains a character and its occurrence number.
    """
    occurance_list = []
    char_occurances = {}
    for char in text:
        if char not in char_occurances:
            char_occurances[char] = 1
        else:
            char_occurances[char] += 1
        num_occurance = char_occurances[char]
        occurance_list.append((char, num_occurance))
    return occurance_list

def inverse_burrows_wheeler_transform(transform: str) -> str:
    """
    Computes the inverse Burrows-Wheeler transform of a string.

    Args:
        transform: The Burrows-Wheeler transform of the string.

    Returns:
        The original string.
    """
    inverse = ""
    last = transform
    first = ''.join(sorted(transform))
    first_list = create_occurance_list(first)
    last_list = create_occurance_list(last)
    current_item = ('$', 1)
    while len(inverse) < len(transform):
        for i in range(len(first_list)):
            if first_list[i] == current_item:
                inverse = current_item[0] + inverse
                current_item = last_list[i]
    return inverse
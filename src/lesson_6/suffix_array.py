"""
This file contains an implementation of the suffix array construction algorithm.
"""

from typing import List, Dict, Iterable, Tuple

def suffix_array(text: str) -> List[int]:
    """
    Constructs the suffix array of a string.

    Args:
        text: The string to construct the suffix array from.

    Returns:
        The suffix array of the string.
    """
    return sorted(range(len(text)), key = lambda i: text[i:])

def main():
    """
    Runs the suffix array construction algorithm.
    """
    seq = "AACGATAGCGGTAGA$"
    print(suffix_array(seq))

if __name__ == "__main__":
    main()
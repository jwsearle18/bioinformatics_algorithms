"""
This file contains a function to find the reverse complement of a DNA string.
"""

def reverse_complement(pattern: str) -> str:
    """
    Finds the reverse complement of a DNA string.

    Args:
        pattern: The DNA string.

    Returns:
        The reverse complement of the DNA string.
    """
    complement = ''
    for nuc in pattern:
        if nuc == 'A':
            complement += 'T'
        elif nuc == 'T':
            complement += 'A'
        elif nuc == 'G':
            complement += 'C'
        elif nuc == 'C':
            complement += 'G'
        else:
            print("Pattern must only contain 'A', 'T', 'G', or 'C'.")
            return
    reverse_complement = complement[::-1]
    return reverse_complement

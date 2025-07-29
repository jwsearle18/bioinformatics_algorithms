"""
This file contains a function to find all neighbors of a string with at most d mismatches.
"""

def hamming_distance(p: str, q: str) -> int:
    """
    Calculates the hamming distance between two strings.

    Args:
        p: The first string.
        q: The second string.

    Returns:
        The hamming distance between the two strings.
    """
    hdist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hdist += 1
    return hdist

def neighbors(s: str, d: int) -> list[str]:
    """
    Finds all neighbors of a string with at most d mismatches.

    Args:
        s: The string.
        d: The maximum number of mismatches.

    Returns:
        A list of all neighbors of the string with at most d mismatches.
    """
    nucleotides = {'A', 'T', 'C', 'G'}
    neighborhood = set()
    if d == 0:
        neighborhood.add(s)
        return neighborhood
    if len(s) == 1:
        neighborhood.update(['A', 'T', 'C', 'G'])
        return neighborhood
    suffixNeighbors = neighbors(s[1:], d)
    for str in suffixNeighbors:
        if hamming_distance(s[1:], str) < d:
            for nuc in nucleotides:
                neighborhood.add(nuc+str)
        else:
            neighborhood.add(s[0]+str)
    return neighborhood
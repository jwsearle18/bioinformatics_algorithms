"""
This file contains functions to find the most frequent k-mers with mismatches and reverse complements in a string.
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
def frequent_words_mismatches_reverse_complements(text: str, k: int, d: int) -> list[str]:
    """
    Finds the most frequent k-mers with mismatches and reverse complements in a string.

    Args:
        text: The string to search.
        k: The length of the k-mers.
        d: The maximum number of mismatches.

    Returns:
        A list of the most frequent k-mers with mismatches and reverse complements.
    """
    rc = reverse_complement(text)
    patterns = []
    freqMap = {}
    for seq in [text, rc]:
        n = len(seq)
        for i in range(n - k + 1):
            pattern = seq[i:i + k]
            neighborhood = neighbors(pattern, d)
            for neighbor in neighborhood:
                if neighbor not in freqMap:
                    freqMap[neighbor] = 1
                else:
                    freqMap[neighbor] += 1

    m = max(freqMap.values())
    for pat in freqMap:
        if freqMap[pat] == m:
            patterns.append(pat)
    return patterns
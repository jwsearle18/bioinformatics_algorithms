from typing import List, Set, Dict, Tuple, Optional

from typing import List, Set

def hamming_distance(p: str, q: str) -> int:
    """
    Calculates the Hamming distance between two strings of equal length.

    Args:
        p: The first string.
        q: The second string.

    Returns:
        The Hamming distance between p and q.
    """
    hdist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hdist += 1
    return hdist

def neighbors(pattern: str, d: int) -> Set[str]:
    """
    Generates the d-neighborhood of a string.
    Args:
        pattern: The string to generate neighbors for.
        d: The maximum Hamming distance.
    Returns:
        A set of all strings that are at most d Hamming distance from pattern.
    """
    neighborhood = {pattern}
    for _ in range(d):
        new_neighbors = set()
        for neighbor in neighborhood:
            for i in range(len(neighbor)):
                for nucleotide in "ACGT":
                    if nucleotide != neighbor[i]:
                        new_neighbor = neighbor[:i] + nucleotide + neighbor[i+1:]
                        new_neighbors.add(new_neighbor)
        neighborhood.update(new_neighbors)
    return neighborhood

def frequent_words_with_mismatches(text: str, k: int, d: int) -> List[str]:
    """
    Finds the most frequent k-mers with at most d mismatches in a string.

    Args:
        text: The string to search.
        k: The length of the k-mers.
        d: The maximum number of mismatches.

    Returns:
        A list of the most frequent k-mers with at most d mismatches.
    """
    patterns = []
    freq_map = {}
    n = len(text)

    for i in range(n - k + 1):
        pattern = text[i:i + k]
        neighborhood = neighbors(pattern, d)
        for neighbor in neighborhood:
            freq_map[neighbor] = freq_map.get(neighbor, 0) + 1

    if not freq_map:
        return []

    max_freq = max(freq_map.values())

    for pattern, freq in freq_map.items():
        if freq == max_freq:
            patterns.append(pattern)

    return patterns

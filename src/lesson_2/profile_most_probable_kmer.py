"""
This file contains a function to find the most probable k-mer in a string, given a profile.
"""

def profile_most_probable_kmer(text: str, k: int,
                               profile: list[dict[str, float]]) -> str:
    """
    Finds the most probable k-mer in a string, given a profile.

    Args:
        text: The string to search.
        k: The length of the k-mer.
        profile: The profile to use. The profile matrix is represented as a list of columns, where the i-th element is a map
    whose keys are strings ("A", "C", "G", and "T") and whose values represent the probability
    associated with this symbol in the i-th column of the profile matrix.

    Returns:
        The most probable k-mer.
    """
    probs = {}
    for i in range(len(text) - k + 1):
        prob = 1
        kmer = text[i:i + k]
        for i in range(k):
            prob *= profile[i][kmer[i]]
        probs[kmer] = prob
    maxProb = max(probs.values())
    for kmer in probs.keys():
        if probs[kmer] == maxProb:
            return kmer
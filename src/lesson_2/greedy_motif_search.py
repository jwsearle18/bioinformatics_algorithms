"""
This file contains functions to find the best motifs in a list of DNA strings using a greedy algorithm.
"""

import sys

def generate_profile(motifs: list[str]) -> list[dict[str, float]]:
    """
    Generates a profile from a list of motifs.

    Args:
        motifs: A list of DNA strings.

    Returns:
        A profile, which is a list of dictionaries. Each dictionary represents a position in the motif and contains the
        frequency of each nucleotide at that position.
    """
    t = len(motifs)
    k = len(motifs[0])
    profile = [{"A":0, "T":0, "C":0, "G":0} for _ in range(k)]
    for i in range(k):
        for motif in motifs:
            profile[i][motif[i]] += 1/t
    return profile

def score(motifs: list[str], profile: list[dict[str, float]]) -> int:
    """
    Calculates the score of a list of motifs.

    The score is the number of mismatches between the motifs and the consensus string.

    Args:
        motifs: A list of DNA strings.
        profile: The profile generated from the motifs.

    Returns:
        The score of the motifs.
    """
    consensus = ""
    count = 0
    for i in range(len(profile)):
        column = profile[i]
        m = max(column.values())
        for key in column.keys():
            if len(consensus) == i:
                if column[key] == m:
                    consensus += key
    for motif in motifs:
        for i in range(len(motif)):
            if motif[i] != consensus[i]:
                count += 1
    return count

def profile_most_probable_kmer(text: str, k: int, profile: list[dict[str, float]]) -> str:
    """
    Finds the most probable k-mer in a string, given a profile.

    Args:
        text: The string to search.
        k: The length of the k-mer.
        profile: The profile to use.

    Returns:
        The most probable k-mer.
    """
    probs = {}
    maxes = []
    for i in range(len(text)-k+1):
        prob = 1
        pattern = text[i:i+k]
        for i in range(k):
            prob = prob * profile[i][pattern[i]]
        probs[pattern] = prob
    mx = max(probs.values())
    for key in probs.keys():
        if probs[key] == mx:
            maxes.append(key)
    return maxes[0]

def greedy_motif_search(dna: list[str], k: int, t: int) -> list[str]:
    """
    Finds the best motifs in a list of DNA strings using a greedy algorithm.

    Args:
        dna: A list of DNA strings.
        k: The length of the motifs to search for.
        t: The number of motifs to search for.

    Returns:
        A list of the best motifs found.
    """
    best_motifs = []
    for string in dna:
        best_motifs.append(string[:k])
    best_score = score(best_motifs, generate_profile(best_motifs))
    for i in range(len(dna[0]) - k + 1):
        motif1 = dna[0][i:i+k]
        motifs = [motif1]
        profile = generate_profile(motifs)
        for i in range(1, t):
            motifs.append(profile_most_probable_kmer(dna[i], k, profile))
            profile = generate_profile(motifs)
        new_score = score(motifs, profile)
        if new_score < best_score:
            best_score = new_score
            best_motifs = motifs
    return best_motifs
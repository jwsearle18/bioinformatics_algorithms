"""
This file contains functions to find the best motifs in a list of DNA strings using the Gibbs sampler algorithm.
"""

import sys 
import random

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
    profile = [{"A":1, "T":1, "C":1, "G":1} for _ in range(k)]
    for i in range(k):
        for motif in motifs:
            profile[i][motif[i]] += 1/t
        for nuc in profile[i]:
            profile[i][nuc] /= (t+4)
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

def profile_weighted_random_kmer(text: str, k: int, profile: list[dict[str, float]]) -> str:
    """
    Finds a random k-mer in a string, weighted by the probability of each k-mer.

    Args:
        text: The string to search.
        k: The length of the k-mer.
        profile: The profile to use.

    Returns:
        A random k-mer, weighted by the probability of each k-mer.
    """
    probs = {}
    for i in range(len(text) - k + 1):
        prob = 1
        kmer = text[i:i + k]
        for i in range(k):
            prob *= profile[i][kmer[i]]
        probs[kmer] = prob
    selectedKmer = random.choices(list(probs.keys()), list(probs.values()), k=1)
    return selectedKmer[0]

def gibbs_sampler(dna: list[str], k: int, t: int, n: int) -> list[str]:
    """
    Finds the best motifs in a list of DNA strings using the Gibbs sampler algorithm.

    Args:
        dna: A list of DNA strings.
        k: The length of the motifs to search for.
        t: The number of motifs to search for.
        n: The number of iterations to run the algorithm for.

    Returns:
        A list of the best motifs found.
    """
    best_motifs = []
    best_score = float('inf')
    for _ in range(20):
        motifs = []
        for string in dna:
            randomStart = random.randint(0, len(string) - k)
            randomKmer = string[randomStart:randomStart + k]
            motifs.append(randomKmer)
        currentMotifs = motifs
        currentBestScore = score(motifs, generate_profile(motifs))
        for _ in range(n):
            i = random.randint(0,t-1)
            newMotifs = currentMotifs.copy()
            newMotifs.pop(i)
            profile = generate_profile(newMotifs)
            motifi = profile_weighted_random_kmer(dna[i], k, profile)
            newMotifs.insert(i, motifi)
            new_score = score(newMotifs, profile)
            if new_score < currentBestScore:
                currentBestScore = new_score
                motifs = newMotifs
        if currentBestScore < best_score:
            best_score = currentBestScore
            best_motifs = motifs

    return best_motifs
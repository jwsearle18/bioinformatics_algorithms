from typing import List, Set, Dict, Tuple, Optional

import sys 
import random

def generate_profile(motifs: list[str]) -> list[dict[str, float]]:
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

'''
10 Outputs:

score: 14
TCGGGGGT ATGTGTAA GTATACAG AGGTGCAC ACGTGCAA
score: 13
AACGGCCA TATGTGTA TAGTACCG TAGATCAA CAGCTCCA
score: 14
CAGTAAAC AAGTGCCA GACCGAAA AGATCAAG ACGTGCAA
score: 13
TGTTCAGT TGCCAAGG TATACAGG CGTCGGTG GCTCCACG
score: 14
TGTTCAGT GGCGAGGT AGTACCGA GTTTCAGG CGTGCAAT
score: 13
GGTGTTCA AAGGTGCC GAAGTATA AAGTTTCA AATGTTGG
score: 13
TCGGGGGT CCAAGGTG TACCGAGA TTCAGGTG TCCACGTG
score: 14
GGGTGTTC AGGTGCCA AAGTATAC CGGTGAAC ATGTTGGC
score: 14
CAGTAAAC AGGTGCCA AGAAGTAT CGGTGAAC AGCTCCAC
score: 13
TCTCGGGG GGGCGAGG TATACAGG GATCAAGT GCTCCACG
'''

'''
Gibb's Sampler in my own words:

Gibb's Sampler is somewhat similar to the random motif search
algorithm, but has a few key differences. The goal of Gibb's Sampler
is to identify implanted motifs in the strings of dna with the lowest
score.  Gibb's sampler is similar to the random motif search in
that it starts with a random selections of 1 motif per sequence.  It
needs several iterations to come to a solid conclusion.  One key
difference is that in Gibb's sampler, 1 motif is removed and replaced
each iteration rather than the entire set of motifs.  The specific 
motif that is removed is random, a profile is built from the remaining
motifs, and a new motif is selected from the sequence of the removed
motif.  This is another key part of the algorithm.  The way this 
motif is selected is by weighted chance based on the weights of the 
profile.  This means it's not entirely deterministic, so it won't always
be the most probable kmer based on the profile, though this kmer is 
most likely to be chosen.  This is key because it allows the search
to potentially get past local minima in wider search for the global
minimum.  After several iterations, the predicted best set of kmers
is the output.

'''

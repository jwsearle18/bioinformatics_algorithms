import sys

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

def profile_most_probable_kmer(text: str, k: int, profile: list[dict[str, float]]) -> str:
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


# Please do not remove package declarations because these are used by the autograder.
# Insert your greedy_motif_search function here, along with any subroutines you need
def greedy_motif_search_pseudocounts(dna: list[str], k: int, t: int) -> list[str]:
    """Implements the GreedyMotifSearch algorithm."""
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
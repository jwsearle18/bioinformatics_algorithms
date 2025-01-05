import sys

def generate_profile(motifs: list[str]) -> list[dict[str, float]]:
    t = len(motifs)
    k = len(motifs[0])
    profile = [{"A":0, "T":0, "C":0, "G":0} for _ in range(k)]
    for i in range(k):
        for motif in motifs:
            profile[i][motif[i]] += 1/t
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


# Please do not remove package declarations because these are used by the autograder.
# Insert your greedy_motif_search function here, along with any subroutines you need
def greedy_motif_search(dna: list[str], k: int, t: int) -> list[str]:
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
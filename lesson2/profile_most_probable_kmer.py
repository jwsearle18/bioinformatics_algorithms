def profile_most_probable_kmer(text: str, k: int,
                               profile: list[dict[str, float]]) -> str:
    """Identifies the most probable k-mer according to a given profile matrix.

    The profile matrix is represented as a list of columns, where the i-th element is a map
    whose keys are strings ("A", "C", "G", and "T") and whose values represent the probability
    associated with this symbol in the i-th column of the profile matrix.
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
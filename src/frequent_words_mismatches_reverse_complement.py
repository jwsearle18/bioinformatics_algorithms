from typing import List, Set, Dict, Tuple, Optional

def reverse_complement(pattern: str) -> str:
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
    hdist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hdist += 1
    return hdist
def neighbors(s: str, d: int) -> list[str]:
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
# Insert your frequent_words_mismatches_reverse_complements function here, along with any subroutines you need
def frequent_words_mismatches_reverse_complements(text: str, k: int, d: int) -> list[str]:
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

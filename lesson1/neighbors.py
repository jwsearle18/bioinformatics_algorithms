def hamming_distance(p: str, q: str) -> int:
    hdist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hdist += 1
    return hdist

# Insert your neighbors function here, along with any subroutines you need
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
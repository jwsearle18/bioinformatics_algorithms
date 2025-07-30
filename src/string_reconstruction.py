from typing import List, Set, Dict, Tuple, Optional

import sys
from typing import List, Dict, Iterable
import random

# Please do not remove package declarations because these are used by the autograder.

def de_bruijn_kmers(k_mers: List[str]) -> tuple[Dict[str, List[str]], str, str]:
    """Forms the de Bruijn graph of a collection of k-mers."""
    adjacency = {}
    in_out = {}
    for i in range(len(k_mers)):
        kmer = k_mers[i]
        prefix = kmer[:len(kmer)-1]
        suffix = kmer[1:]
        if prefix not in adjacency.keys():
            adjacency[prefix] = [suffix]
        else:
            adjacency[prefix].append(suffix)
        if suffix not in in_out.keys():
            in_out[suffix] = [1, 0]
        else:
            in_out[suffix][0] = in_out[suffix][0] + 1
        if prefix not in in_out.keys():
            in_out[prefix] = [0, 1]
        else:
            in_out[prefix][1] = in_out[prefix][1] + 1
    start = ""
    end = ""
    for key in in_out.keys():
        num_in = in_out[key][0]
        num_out = in_out[key][1]
        if num_out - num_in > 0:
            start = key
        elif num_out - num_in < 0:
            end = key
    if end != "":
        if end not in adjacency.keys():
            adjacency[end] = [start]
        else:
            adjacency[end].append(start)
    return adjacency, start, end

def create_cycle(g: Dict[str, List[str]], ordered: bool, cycle=[], start = "") -> List[str]:
    if cycle == []:
        start = random.choice(list(g.keys()))
    cycle.append(start)
    while True:
        if len(g[start]) > 0:
            next = random.choice(g[start])
            g[start].remove(next)
            cycle.append(next)
            start = next
        else:
            for key in list(g.keys()):
                if len(g[key]) == 0:
                    del g[key]
            if ordered:
                return cycle[:-1]
            else:
                return cycle

# Insert your string_reconstruction function here, along with any subroutines you need
def string_reconstruction(patterns: List[str], k: int) -> str:
    """Reconstructs a string from its k-mer composition."""
    g, start, end = de_bruijn_kmers(patterns)
    if start == "":
        ordered = False
    else:
        ordered = True
    cycle = create_cycle(g, ordered)
    while len(g) > 0:
        for _ in range(len(cycle)):
            if cycle[0] not in g.keys():
                rotation = cycle.pop(0)
                cycle.append(rotation)
            else:
                next_start = cycle[0]
                break
        
        cycle = create_cycle(g, ordered, cycle, next_start)
    if start != "":
        for _ in range(len(cycle)):
            if cycle[0] != start or cycle[-1] != end:
                rotation = cycle.pop(0)
                cycle.append(rotation)
    reconstructed_string = cycle[0]
    for i in range(1, len(cycle)):
        reconstructed_string = reconstructed_string+cycle[i][-1]
    return reconstructed_string

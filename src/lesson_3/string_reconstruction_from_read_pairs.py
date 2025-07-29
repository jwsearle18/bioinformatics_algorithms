"""
This file contains functions to reconstruct a string from a collection of read-pairs.
"""

import sys
from typing import List, Dict, Iterable, Tuple
import random

def de_bruijn_kmers(PairedReads: List[Tuple[str, str]]) -> Tuple[Dict[Tuple[str, str], List[Tuple[str, str]]], str, str]:
    """
    Forms the de Bruijn graph of a collection of k-mers.

    Args:
        PairedReads: A list of read-pairs.

    Returns:
        A tuple containing the adjacency list of the de Bruijn graph, the start node of the Eulerian path, and the end
        node of the Eulerian path.
    """
    adjacency = {}
    in_out = {}
    for i in range(len(PairedReads)):
        read1 = PairedReads[i][0]
        read2 = PairedReads[i][1]
        prefix1 = read1[:len(read1)-1]
        suffix1 = read1[1:]
        prefix2 = read2[:len(read2)-1]
        suffix2 = read2[1:]
        prefixTuple = (prefix1, prefix2)
        suffixTuple = (suffix1, suffix2)
        if prefixTuple not in adjacency.keys():
            adjacency[prefixTuple] = [suffixTuple]
        else:
            adjacency[prefixTuple].append(suffixTuple)
        if suffixTuple not in in_out.keys():
            in_out[suffixTuple] = [1, 0]
        else:
            in_out[suffixTuple][0] = in_out[suffixTuple][0] + 1
        if prefixTuple not in in_out.keys():
            in_out[prefixTuple] = [0, 1]
        else:
            in_out[prefixTuple][1] = in_out[prefixTuple][1] + 1
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
    """
    Creates a cycle in a graph.

    Args:
        g: The graph.
        ordered: A boolean indicating whether the cycle should be ordered.
        cycle: The current cycle.
        start: The start node of the cycle.

    Returns:
        The cycle.
    """
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

def StringReconstructionReadPairs(PairedReads: List[Tuple[str, str]], k: int, d: int) -> str:
    """
    Reconstructs a string from a collection of read-pairs.

    Args:
        PairedReads: A list of read-pairs.
        k: The length of the k-mers.
        d: The distance between the read-pairs.

    Returns:
        The reconstructed string.
    """
    is_correct = False
    
    while is_correct == False:    
        g, start, end = de_bruijn_kmers(PairedReads)
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

        read1 = cycle[0][0]
        read2 = cycle[0][1]
        for i in range(1, len(cycle)):
            read1 += cycle[i][0][-1]
            read2 += cycle[i][1][-1]

        if read1[k+d:] == read2[:-k-d]:
            is_correct = True
    
    reconstructed_string = read1 + read2[-k-d:]
    return reconstructed_string
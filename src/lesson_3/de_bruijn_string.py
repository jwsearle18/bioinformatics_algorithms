"""
This file contains a function to construct a de Bruijn graph from a string.
"""

import sys
from typing import List, Dict, Iterable

def de_bruijn_string(text: str, k: int) -> Dict[str, List[str]]:
    """
    Constructs a de Bruijn graph from a string.

    Args:
        text: The string to construct the graph from.
        k: The length of the k-mers to use.

    Returns:
        A dictionary representing the adjacency list of the de Bruijn graph.
    """
    adjacencyDict = {}
    nodeList = []

    for i in range(len(text) - k + 1):
        node = text[i:i + k - 1]
        nodeList.append(node)
    nodeList = sorted(list(set(nodeList)))

    for node in nodeList:
        adjacencyDict[node] = []
    
    for i in range(len(text) - k + 1):
        node = text[i:i + k - 1]
        if i + 2*k - (k - 1) <= len(text) + 1:
            nextNode = text[i + k - (k - 1):i + k]
        else:
            nextNode = None
        if nextNode != None:
            adjacencyDict[node].append(nextNode)
            adjacencyDict[node].sort()
    return adjacencyDict
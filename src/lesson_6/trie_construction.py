"""
This file contains an implementation of the trie construction algorithm.
"""

from typing import List, Dict, Tuple

def trie_construction(patterns: List[str]) -> List[Tuple[int, int, str]]:
    """
    Constructs a trie from a list of patterns.

    Args:
        patterns: The patterns to construct the trie from.

    Returns:
        A list of tuples representing the edges of the trie.
    """
    trie_dict = {0:{}}
    trie = []
    nextNode = 0
    for pattern in patterns:
        currentNode = 0
        for i in range(len(pattern)):
            currentNuc = pattern[i]
            if currentNuc in trie_dict[currentNode]:
                currentNode = trie_dict[currentNode][currentNuc]

            else:
                nextNode += 1
                trie_dict[currentNode][currentNuc] = nextNode
                trie_dict[nextNode] = {}
                trie.append((currentNode, nextNode, currentNuc))
                currentNode = nextNode
    
    return sorted(trie, key = lambda x: x[0])

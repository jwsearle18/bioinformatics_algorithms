from typing import List, Set, Dict, Tuple, Optional

import sys
from typing import List, Dict, Iterable

def de_bruijn_string(text: str, k: int) -> Dict[str, List[str]]:
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

from typing import List, Dict, Tuple

def trie_construction(patterns: List[str]) -> List[Tuple[int, int, str]]:
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

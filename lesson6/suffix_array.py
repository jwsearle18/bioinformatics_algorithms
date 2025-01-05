from typing import List, Dict, Iterable, Tuple

def suffix_array(text: str) -> List[int]:
    return sorted(range(len(text)), key = lambda i: text[i:])

seq = "AACGATAGCGGTAGA$"
print(suffix_array(seq))
import sys
from typing import List, Dict, Iterable, Tuple

def burrows_wheeler_transform(text: str) -> str:
    suffixes = []
    transform = ""
    for i in range(len(text)):
        suffixes.append(text[i:] + text[:i])
    suffixes = sorted(suffixes)
    for suffix in suffixes:
        transform += suffix[-1]
    return transform
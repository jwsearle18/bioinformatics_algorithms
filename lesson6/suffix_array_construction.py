import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your suffix_array function here, along with any subroutines you need
def suffix_array(text: str) -> List[int]:
    suffixes = []
    for i in range(len(text)):
        suffixes.append([text[i:], i])
    suffixes = sorted(suffixes)
    formated = []
    for suffix in suffixes:
        formated.append(suffix[1])
    return formated
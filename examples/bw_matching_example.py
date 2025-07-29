import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your bw_matching function here, along with any subroutines you need
def better_bw_matching(bwt: str, patterns: List[str]) -> List[int]:
    first = list(bwt)
    first.sort()
    count = get_count(bwt)
    
    matches = []
    for pattern in patterns:
        top = 0
        bottom = len(bwt) - 1
        while top <= bottom:
            if pattern != "":
                curr_symbol = pattern[-1]
                pattern = pattern[:-1]
                bwt_i = [j for j in range(top, bottom+1) if bwt[j] == curr_symbol]
                if len(bwt_i) > 0:
                    top = first.index(curr_symbol) + count[curr_symbol][top]
                    bottom = first.index(curr_symbol) + count[curr_symbol][bottom + 1] - 1
                else:
                    matches.append(0)
                    break
            else:
                matches.append(bottom - top + 1)
                break
    return matches

def get_count(bwt):
    chars = {}
    i = 1
    for char in bwt:
        if char not in chars:
            chars[char] = [0] * (len(bwt) + 1)
        for j in range(i, len(bwt) + 1):
            chars[char][j] += 1
        i += 1
    return chars


bwt = "GGCGCCGC$TAGTCACACACGCCGTA"
patterns = ["ACC", "CCG", "CAG"]

matches = better_bw_matching(bwt, patterns)
print(matches)
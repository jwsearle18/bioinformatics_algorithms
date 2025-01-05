import sys
from typing import List, Dict, Iterable, Tuple

def create_occurance_list(text: str) -> List[Tuple[str, int]]:
    occurance_list = []
    char_occurances = {}
    for char in text:
        if char not in char_occurances:
            char_occurances[char] = 1
        else:
            char_occurances[char] += 1
        num_occurance = char_occurances[char]
        occurance_list.append((char, num_occurance))
    return occurance_list

def create_last_to_first(first: List, last: List) -> List[int]:
    last_to_first = []
    first_index_dict = {}
    for i in range(len(first)):
        first_index_dict[first[i]] = i
    for item in last:
        last_to_first.append(first_index_dict[item])
    return last_to_first


def bw_matching(bwt: str, patterns: List[str]) -> List[int]:
    bw_matches = []
    last = bwt
    first = ''.join(sorted(bwt))
    first_list = create_occurance_list(first)
    last_list = create_occurance_list(last)
    last_to_first = create_last_to_first(first_list, last_list)
    for pattern in patterns:
        top = 0
        bottom = len(last) - 1
        while top <= bottom:
            if pattern:
                symbol = pattern[-1]
                pattern = pattern[:-1]
                section = last[top:bottom+1]
                if symbol in section:
                    for i in range(len(section)):
                        if section[i] == symbol:
                            top_index = top + i
                            break
                    for i in range(len(section) -1, -1, -1):
                        if section[i] == symbol:
                            bottom_index = top + i
                            break
                    top = last_to_first[top_index]
                    bottom = last_to_first[bottom_index]
                else:
                    bw_matches.append(0)
                    break
            else:
                bw_matches.append(bottom-top+1)
                break
    return bw_matches
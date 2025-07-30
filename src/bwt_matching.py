from typing import List, Tuple, Dict

def create_occurrence_list(text: str) -> List[Tuple[str, int]]:
    """
    Creates a list of tuples of (character, occurrence) for a string.

    Args:
        text: The input string.

    Returns:
        A list of tuples, where each tuple is (character, occurrence count).
    """
    occurrence_list = []
    char_occurrences: Dict[str, int] = {}
    for char in text:
        char_occurrences[char] = char_occurrences.get(char, 0) + 1
        num_occurrence = char_occurrences[char]
        occurrence_list.append((char, num_occurrence))
    return occurrence_list

def create_last_to_first(first: List[Tuple[str, int]], last: List[Tuple[str, int]]) -> List[int]:
    """
    Creates the last-to-first mapping for the Burrows-Wheeler Transform.

    Args:
        first: The first column of the BWT matrix as a list of (char, occurrence).
        last: The last column of the BWT matrix as a list of (char, occurrence).

    Returns:
        A list representing the last-to-first mapping.
    """
    last_to_first = [-1] * len(last)
    first_index_dict: Dict[Tuple[str, int], int] = {val: i for i, val in enumerate(first)}
    for i, item in enumerate(last):
        last_to_first[i] = first_index_dict[item]
    return last_to_first


def bwt_matching(bwt: str, patterns: List[str]) -> List[int]:
    """
    Performs pattern matching using the Burrows-Wheeler Transform.

    Args:
        bwt: The Burrows-Wheeler Transform string.
        patterns: A list of patterns to search for.

    Returns:
        A list of the number of matches for each pattern.
    """
    last_col = bwt
    first_col = "".join(sorted(bwt))

    first_list = create_occurrence_list(first_col)
    last_list = create_occurrence_list(last_col)

    last_to_first = create_last_to_first(first_list, last_list)

    bw_matches = []

    for pattern in patterns:
        top = 0
        bottom = len(last_col) - 1

        while top <= bottom:
            if pattern:
                symbol = pattern[-1]
                pattern = pattern[:-1]

                section = last_col[top : bottom + 1]

                if symbol in section:
                    top_index = -1
                    bottom_index = -1

                    for i in range(len(section)):
                        if section[i] == symbol:
                            if top_index == -1:
                                top_index = top + i
                            bottom_index = top + i

                    top = last_to_first[top_index]
                    bottom = last_to_first[bottom_index]
                else:
                    bw_matches.append(0)
                    break
            else:
                bw_matches.append(bottom - top + 1)
                break

    return bw_matches

if __name__ == '__main__':
    bwt = "GGCGCCGC$TAGTCACACACGCCGTA"
    patterns = ["ACC", "CCG", "CAG"]
    matches = bwt_matching(bwt, patterns)
    print(f"The matches are: {matches}")

from typing import List, Dict

def get_count(bwt: str) -> Dict[str, List[int]]:
    """
    Calculates the count of each character in the Burrows-Wheeler Transform string.

    Args:
        bwt: The Burrows-Wheeler Transform string.

    Returns:
        A dictionary where keys are characters and values are lists of counts.
    """
    chars = {}
    for char in set(bwt):
        chars[char] = [0] * (len(bwt) + 1)

    for i, char in enumerate(bwt):
        for c in chars:
            chars[c][i+1] = chars[c][i]
        chars[char][i+1] += 1

    return chars

def better_bwt_matching(bwt: str, patterns: List[str]) -> List[int]:
    """
    Performs pattern matching using the Burrows-Wheeler Transform.

    Args:
        bwt: The Burrows-Wheeler Transform string.
        patterns: A list of patterns to search for.

    Returns:
        A list of the number of matches for each pattern.
    """
    first_col = "".join(sorted(bwt))
    count = get_count(bwt)

    matches = []

    for pattern in patterns:
        top = 0
        bottom = len(bwt) - 1

        while top <= bottom:
            if pattern:
                symbol = pattern[-1]
                pattern = pattern[:-1]

                if symbol in bwt[top:bottom+1]:
                    top = first_col.find(symbol) + count[symbol][top]
                    bottom = first_col.find(symbol) + count[symbol][bottom + 1] - 1
                else:
                    matches.append(0)
                    break
            else:
                matches.append(bottom - top + 1)
                break

    return matches

if __name__ == "__main__":
    bwt = "GGCGCCGC$TAGTCACACACGCCGTA"
    patterns = ["ACC", "CCG", "CAG"]
    matches = better_bwt_matching(bwt, patterns)
    print(f"The matches are: {matches}")

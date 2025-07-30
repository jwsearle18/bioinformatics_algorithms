from typing import List

def burrows_wheeler_transform(text: str) -> str:
    """
    Computes the Burrows-Wheeler Transform of a string.

    Args:
        text: The input string.

    Returns:
        The Burrows-Wheeler Transform of the string.
    """
    # Create a list of all rotations of the string
    rotations = [text[i:] + text[:i] for i in range(len(text))]

    # Sort the rotations lexicographically
    rotations.sort()

    # Take the last character of each rotation
    bwt = "".join([rotation[-1] for rotation in rotations])

    return bwt

if __name__ == '__main__':
    text = "GCGTGCCTGGTCA$"
    bwt = burrows_wheeler_transform(text)
    print(f"The Burrows-Wheeler Transform of {text} is {bwt}")

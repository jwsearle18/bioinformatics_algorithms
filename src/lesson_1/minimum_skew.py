"""
This file contains a function to find the minimum skew of a DNA string.
"""
def minimum_skew(genome: str) -> list[int]:
    """
    Finds the minimum skew of a DNA string.

    The skew of a DNA string is the difference between the total number of occurrences of G and C.

    Args:
        genome: The DNA string.

    Returns:
        A list of all positions in the DNA string where the skew is minimized.
    """
    skew = [0]
    for i in range(len(genome)):
        if genome[i] == 'G':
            skew.append(skew[i]+1)
        elif genome[i] == 'C':
            skew.append(skew[i]-1)
        else:
            skew.append(skew[i])
    min_value = min(skew)
    min_positions = []
    for i in range(len(skew)):
        if skew[i] == min_value:
            min_positions.append(i)
    return min_positions
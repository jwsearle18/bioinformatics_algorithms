from typing import List, Set, Dict, Tuple, Optional

def calculate_gc_content(dna_string: str) -> float:
    """
    Calculates the GC content of a DNA string.

    Args:
        dna_string: A string representing a DNA sequence.

    Returns:
        The GC content as a percentage.
    """
    gc_count = dna_string.count('G') + dna_string.count('C')
    return (gc_count / len(dna_string)) * 100 if len(dna_string) > 0 else 0.0

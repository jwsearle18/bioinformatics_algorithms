from typing import List, Set, Dict, Tuple, Optional

def reverse_complement(pattern: str) -> str:
    complement = ''
    for nuc in pattern:
        if nuc == 'A':
            complement += 'T'
        elif nuc == 'T':
            complement += 'A'
        elif nuc == 'G':
            complement += 'C'
        elif nuc == 'C':
            complement += 'G'
        else:
            print("Pattern must only contain 'A', 'T', 'G', or 'C'.")
            return
    reverse_complement = complement[::-1]
    return reverse_complement

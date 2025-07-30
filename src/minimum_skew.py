from typing import List, Set, Dict, Tuple, Optional

def minimum_skew(genome: str) -> list[int]:
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

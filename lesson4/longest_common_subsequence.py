import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

sys.setrecursionlimit(10000) # Don't delete! This line is useful to ensure you have sufficient "recursion depth" to store the recursive calls needed for this problem.

def LCSbacktrack(v: str, w: str) -> List[List[int]]:
    numRows = len(v)
    numCols = len(w)
    
    back_track = []
    s = []
    for _ in range(numCols + 1): 
        back_track_row = [0 for _ in range(numRows + 1)]
        back_track.append(back_track_row)
        s_row = [0 for _ in range(numRows + 1)]
        s.append(s_row)
    for row in range(1, numCols + 1):
        for col in range(1, numRows + 1):
            match = 0           
            down = s[row - 1][col]
            right = s[row][col - 1]
            if v[col-1] == w[row-1]:
                match = 1
                diagonal = s[row-1][col-1] + match
            else:
                diagonal = s[row-1][col-1]
            
            max_val = max([down, right, diagonal])
            s[row][col] = max_val
            if max_val == down:
                back_track[row][col] = 1
            elif max_val == right:
                back_track[row][col] = 2
            else:
                back_track[row][col] = 0      
    return back_track

def outputLCS(back_track: List[List[int]], v: str, i: int, j: int) -> str:
    if i==0 or j==0:
        return ''
    if back_track[j][i] == 1:
        return outputLCS(back_track, v, i, j-1)
    elif back_track[j][i] == 2:
        return outputLCS(back_track, v, i-1, j)
    else:
        return outputLCS(back_track, v, i-1, j-1) + v[i-1]
    
def longest_common_subsequence(s: str, t: str) -> str:
    back_track = LCSbacktrack(s, t)
    return outputLCS(back_track, s, len(s), len(t))
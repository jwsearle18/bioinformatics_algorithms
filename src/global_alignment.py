from typing import List, Set, Dict, Tuple, Optional

import sys
from typing import List, Dict, Tuple

def create_matrix(match_reward: int, mismatch_penalty: int, indel_penalty: int, s: str, t: str) -> Tuple[int, List[List[int]]]:
    v = len(s)
    w = len(t)
    matrix = []
    back_track = []
    for _ in range(w+1):
        matrix_row = [0 for _ in range(v + 1)]
        back_track_row = [0 for _ in range(v + 1)]
        matrix.append(matrix_row)
        back_track.append(back_track_row)
    for row in range(w+1):
        for column in range(v+1):
            if row == 0 and column == 0:
                continue
            elif row == 0:
                right = matrix[row][column - 1] - indel_penalty
                down = right - 1
                diagonal = right - 1
            elif column == 0:
                down = matrix[row-1][column] - indel_penalty
                right = down - 1
                diagonal = down - 1
            else:
                down = matrix[row - 1][column] - indel_penalty
                right = matrix[row][column - 1] - indel_penalty
                if s[column-1] == t[row-1]:
                    diagonal = matrix[row-1][column-1] + match_reward
                else:
                    diagonal = matrix[row-1][column-1] - mismatch_penalty
            max_val = max([down, right, diagonal])
            if down == max_val:
                matrix[row][column] = down
                back_track[row][column] = 1
            elif right == max_val:
                matrix[row][column] = right
                back_track[row][column] = 2
            else:
                matrix[row][column] = max_val
                back_track[row][column] = 0
    return max_val, back_track

def global_alignment(match_reward: int, mismatch_penalty: int, indel_penalty: int, s: str, t: str) -> Tuple[int, str, str]:
    max_val, back_track = create_matrix(match_reward, mismatch_penalty, indel_penalty, s, t)
    first_string = ""
    second_string = ""
    v = len(s)
    w = len(t)
    while v != 0 or w != 0:
        direction = back_track[w][v]
        if direction == 0:
            first_string += s[v-1]
            second_string += t[w-1]
            v -= 1
            w -= 1
        elif direction == 1:
            second_string += t[w-1]
            first_string += "-"
            w -= 1
        else:
            first_string += s[v-1]
            second_string += "-"
            v -= 1
    return max_val, first_string[::-1], second_string[::-1]

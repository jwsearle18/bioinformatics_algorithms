from typing import List, Set, Dict, Tuple, Optional

import sys
from typing import List, Tuple

def create_matrix(match_reward: int, mismatch_penalty: int, indel_penalty: int, s: str, t: str) -> Tuple[List[Tuple], Tuple ,int, List[List[int]]]:
    v = len(s)
    w = len(t)
    matrix = []
    back_track = []
    for _ in range(w+1):
        matrix_row = [0 for _ in range(v + 1)]
        back_track_row = [0 for _ in range(v + 1)]
        matrix.append(matrix_row)
        back_track.append(back_track_row)

    possible_end_pos_list = []
    matrix_max_val = float('-inf')
    pos_max_val = (v+1, w+1)
    for row in range(1, w+1):
        for column in range(1, v+1):
            down = matrix[row - 1][column] - indel_penalty
            right = matrix[row][column - 1] - indel_penalty
            if s[column-1] == t[row-1]:
                diagonal = matrix[row-1][column-1] + match_reward
            else:
                diagonal = matrix[row-1][column-1] - mismatch_penalty
            
            max_val = max([0, down, right, diagonal])
            matrix[row][column] = max_val

            if down == max_val:
                back_track[row][column] = 1
            elif right == max_val:
                back_track[row][column] = 2
            else:
                back_track[row][column] = 0
            if matrix[row][column] > matrix_max_val:
                pos_max_val = (row, column)
                matrix_max_val = matrix[row][column]
            if matrix[row][column] == 0:
                possible_end_pos_list.append((row, column))
    return possible_end_pos_list, pos_max_val, matrix_max_val, back_track

def local_alignment(match_reward: int, mismatch_penalty: int, indel_penalty: int, s: str, t: str) -> Tuple[int, str, str]:
    possible_end_pos_list, pos_max_val, matrix_max_val, back_track = create_matrix(match_reward, mismatch_penalty, indel_penalty, s, t)
    first_string = ""
    second_string = ""

    start_row = pos_max_val[0]
    start_column = pos_max_val[1]
    while start_row > 0 and start_column > 0 and (start_row, start_column) not in possible_end_pos_list:
        direction = back_track[start_row][start_column]
        if direction == 0:
            first_string += s[start_column - 1]
            second_string += t[start_row - 1]
            start_row -= 1
            start_column -= 1
        elif direction == 1:
            first_string += "-"
            second_string += t[start_row - 1]
            start_row -= 1
        else:
            first_string += s[start_column - 1]
            second_string += "-"
            start_column -= 1
    return matrix_max_val, first_string[::-1], second_string[::-1]

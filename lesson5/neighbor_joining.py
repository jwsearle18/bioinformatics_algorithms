"""Neighbor-Joining phylogenetic tree algorithm."""
import pandas as pd # type: ignore

def get_delta(TotalDist: list, n: int, i: int, j: int):
    return (TotalDist[i] - TotalDist[j]) / (n - 2)

def get_matrix_min_pos(matrix: pd.DataFrame):
    min_value = float('inf')
    min_value_pos = (-1, -1)
    for i in matrix.index:
        for j in matrix.columns:
            if i != j and matrix.loc[i, j] < min_value:
                min_value = matrix.loc[i, j]
                min_value_pos = (i, j)

    return min_value_pos
    
def get_limb_length_i(matrix: pd.DataFrame, i: int, j: int, delta: float):
    return (1/2) * (matrix.loc[i, j] + delta)

def get_limb_length_j(matrix: pd.DataFrame, i: int, j: int, delta: float):
    return (1/2) * (matrix.loc[i, j] - delta)

def calculate_new_D_km(D: pd.DataFrame, k: int, i: int, j: int):
    return (1/2) * (D.loc[k, i] + D.loc[k, j] - D.loc[i, j])

def NeighborJoining(n: int, D: pd.DataFrame, current_m: int) -> dict[int, dict[int, float]]:
    tree = {}
    
    if n == 2:
        tree[D.columns[0]] = {D.columns[1]: D.at[D.columns[0], D.columns[1]]}
        tree[D.columns[1]] = {D.columns[0]: D.at[D.columns[1], D.columns[0]]}
        return tree
    
    TotalDist_D = D.sum().tolist()
    
    D_star = pd.DataFrame(0, index=D.index, columns=D.columns)
    for i in D.index:
        for j in D.columns:
            if i != j:
                D_star.loc[i, j] = (n - 2) * D.loc[i, j] - TotalDist_D[D.index.get_loc(i)] - TotalDist_D[D.columns.get_loc(j)]
    
    i, j = get_matrix_min_pos(D_star)
    
    delta = get_delta(TotalDist_D, n, D.index.get_loc(i), D.index.get_loc(j))
    limb_length_i = get_limb_length_i(D, i, j, delta)
    limb_length_j = get_limb_length_j(D, i, j, delta)

    new_D = D.drop(index=[i, j], columns=[i, j])

    new_m = current_m

    new_row_col = []
    for k in new_D.index:
        D_km = calculate_new_D_km(D, k, i, j)
        new_row_col.append(D_km)
    
    new_D[new_m] = new_row_col
    new_row_col.append(0)
    new_D.loc[new_m] = new_row_col

    D = new_D
    n = len(D)

    tree = NeighborJoining(n, D, current_m + 1)

    if i not in tree:
        tree[i] = {}
    if j not in tree:
        tree[j] = {}
    if new_m not in tree:
        tree[new_m] = {}
    
    tree[new_m][i] = limb_length_i
    tree[new_m][j] = limb_length_j
    tree[i][new_m] = limb_length_i
    tree[j][new_m] = limb_length_j

    return tree


with open('dataset_40204_6.txt', 'r') as file:
    lines = []
    for line in file:
        lines.append(line)

n = int(lines[0].strip())
D = []
for line in lines[1:]:
    row = list(map(int, line.split()))
    D.append(row)

D = pd.DataFrame(D)
D.columns = range(n)
D.index = range(n)

current_m = n

myTree = NeighborJoining(n, D, current_m)

def displayTree(tree):
    for key in sorted(tree.keys()):
        for value in tree[key]:
            print(f'{key}->{value}:{tree[key][value]:.3f}')

displayTree(myTree)


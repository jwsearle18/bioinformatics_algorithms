from typing import List, Set, Dict, Tuple, Optional

import copy
with open("dataset_40207_6.txt", "r") as text:
    input_text = text.read().splitlines(True)
line_1 = input_text[0].strip().split()
a = line_1[0]
b = line_1[1]
input_text = input_text[1:]
tree = {}
for relationship in input_text:
    relationship = relationship.strip().split(sep = "->")
    if relationship[0] in tree:
        tree[relationship[0]].append(relationship[1])
    else:
        tree[relationship[0]] = [relationship[1]]

a_edges = [edge for edge in tree[a] if edge != b]
b_edges = [edge for edge in tree[b] if edge != a]

def Swap(tree, a, b, a_edge, b_edge):
    new_tree = copy.deepcopy(tree)
    new_tree[a].remove(a_edge)
    new_tree[a].append(b_edge)
    new_tree[b].remove(b_edge)
    new_tree[b].append(a_edge)
    new_tree[a_edge].remove(a)
    new_tree[a_edge].append(b)
    new_tree[b_edge].remove(b)
    new_tree[b_edge].append(a)
    return new_tree

tree1 = Swap(tree, a, b, a_edges[1], b_edges[0])
tree2 = Swap(tree, a, b, a_edges[1], b_edges[1])

for key in tree1:
    current_list = tree1[key]
    for item in current_list:
        print(f"{key}->{item}")
print()
for key in tree2:
    current_list = tree2[key]
    for item in current_list:
        print(f"{key}->{item}")

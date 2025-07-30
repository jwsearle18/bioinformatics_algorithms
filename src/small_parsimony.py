from typing import List, Set, Dict, Tuple, Optional

import sys

class Node:
    def __init__(self, name, parent=None, child1=None, child2=None, final_score=0, current_num_change=None, sequence="", original_sequence="", leaf=True, child_nucs=None):
        self.child1 = child1
        self.child2 = child2
        self.final_score = final_score
        self.sequence = sequence
        self.original_sequence = original_sequence
        self.parent = parent
        self.name = name
        self.leaf = leaf
        self.current_num_change = current_num_change if current_num_change is not None else {}
        self.child_nucs = child_nucs if child_nucs is not None else {}

    def add_child1(self, child):
        self.child1 = child

    def add_child2(self, child):
        self.child2 = child

    def add_parent(self, parent):
        self.parent = parent

    def not_leaf(self):
        self.leaf = False

    def update_sequence(self, sequence: str):
        self.sequence = sequence

    def update_current_num_change(self, current_num_change):
        self.current_num_change = current_num_change

    def update_child_nucs(self, child_nucs):
        self.child_nucs = child_nucs

    def __repr__(self):
        return f"Node(name: {self.name}, parent: {self.parent.name if self.parent else 'None'}, child1: {self.child1.name if self.child1 else 'None'}, child2: {self.child2.name if self.child2 else 'None'}, leaf: {self.leaf}, sequence: {self.sequence}, number of change: {self.current_num_change}, child_nucs:{self.child_nucs})"

with open(sys.argv[1], "r") as text:
    input_data = text.read().strip().splitlines(True)

n = int(input_data[0].strip())
nodes = {}
tree = []
leaf_counter = {}

for row in input_data[1:]:
    row = row.strip().split(sep="->")
    parent_name, child_name = row[0], row[1]
    if parent_name not in nodes:
        parent_node = Node(name=parent_name, leaf=False)
        nodes[parent_name] = parent_node
        tree.append(parent_node)
    else:
        parent_node = nodes[parent_name]

    if child_name.isdigit():
        if child_name not in nodes:
            child_node = Node(name=child_name, leaf=False)
            nodes[child_name] = child_node
            tree.append(child_node)
        else:
            child_node = nodes[child_name]
    else:
        if child_name not in leaf_counter:
            leaf_counter[child_name] = 0
        leaf_counter[child_name] += 1
        child_node = Node(name=f"{child_name}_{leaf_counter[child_name]}", leaf=True, original_sequence=child_name)
        nodes[child_node.name] = child_node
        tree.append(child_node)
    child_node.add_parent(parent_node)
    if parent_node.child1 is None:
        parent_node.add_child1(child_node)
    elif parent_node.child2 is None:
        parent_node.add_child2(child_node)
for node in tree:
    if node.leaf:
        sequence_length = len(node.original_sequence)
        break 

def backtrack_nucs(Tree, node, parent_nuc):
    if node.leaf:
        return
    node_nuc = parent_nuc
    if node.child1:
        child1_nucs = node.child_nucs[node_nuc][0]
        child1_nuc = child1_nucs[0]
        node.child1.update_sequence(node.child1.sequence + child1_nuc)
        backtrack_nucs(Tree, node.child1, child1_nuc)
    if node.child2:
        child2_nucs = node.child_nucs[node_nuc][1]
        child2_nuc = child2_nucs[0]
        node.child2.update_sequence(node.child2.sequence + child2_nuc)
        backtrack_nucs(Tree, node.child2, child2_nuc)

def SmallParsimony(node, index):
    if node.leaf:
        sequence = node.original_sequence
        current_nucleotide = sequence[index]
        current_num_change = {}
        for nuc in ["A", "T", "C", "G"]:
            if nuc == current_nucleotide:
                current_num_change[nuc] = 0
            else:
                current_num_change[nuc] = float('inf')
        node.update_current_num_change(current_num_change)
    else:
        SmallParsimony(node.child1, index)
        SmallParsimony(node.child2, index)
        current_num_change = {}
        child_nucs = {}
        child1_num_change = node.child1.current_num_change
        child2_num_change = node.child2.current_num_change
        for k in ["A", "T", "C", "G"]:
            min_s1 = float('inf')
            s1_nucs = []
            for a in ["A", "T", "C", "G"]:
                distance = 0 if k == a else 1
                s = child1_num_change[a] + distance
                if s < min_s1:
                    min_s1 = s
                    s1_nucs = [a]
                elif s == min_s1:
                    s1_nucs.append(a)
            min_s2 = float('inf')
            s2_nucs = []
            for b in ["A", "T", "C", "G"]:
                distance = 0 if k == b else 1
                s = child2_num_change[b] + distance
                if s < min_s2:
                    min_s2 = s
                    s2_nucs = [b]
                elif s == min_s2:
                    s2_nucs.append(b)
            current_num_change[k] = min_s1 + min_s2
            child_nucs[k] = [s1_nucs, s2_nucs]
        node.update_current_num_change(current_num_change)
        node.update_child_nucs(child_nucs)

def hamming_distance(p: str, q: str) -> int:
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

def WholeSmallParsimony(Tree, sequence_length):
    score = 0
    relationships = []
    root = [node for node in Tree if node.parent is None][0]
    for i in range(sequence_length):
        for node in Tree:
            if not node.leaf:
                node.sequence = node.sequence[:i]
        SmallParsimony(root, i)
        root_min_score = min(root.current_num_change.values())
        root_nucs = [k for k in root.current_num_change if root.current_num_change[k] == root_min_score]
        root_nuc = root_nucs[0]
        root.update_sequence(root.sequence + root_nuc)
        backtrack_nucs(Tree, root, root_nuc)
    for node in Tree:
        sequence = node.sequence
        if node.child1:
            child1_sequence = node.child1.sequence
            child1_score = hamming_distance(sequence, child1_sequence)
            relationships.append([f"{sequence}->{child1_sequence}", child1_score])
            score += child1_score
        if node.child2:
            child2_sequence = node.child2.sequence
            child2_score = hamming_distance(sequence, child2_sequence)
            relationships.append([f"{sequence}->{child2_sequence}", child2_score])
            score += child2_score
        if node.parent:
            parent_sequence = node.parent.sequence
            parent_score = hamming_distance(sequence, parent_sequence)
            relationships.append([f"{sequence}->{parent_sequence}", parent_score])
            score += parent_score
    print(int(score/2))
    relationships = sorted(relationships)
    for i in relationships:
        print(f"{i[0]}:{i[1]}")

WholeSmallParsimony(tree, sequence_length)

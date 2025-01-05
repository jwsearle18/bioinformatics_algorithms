from typing import List, Dict, Tuple
import pandas as pd # type: ignore

def populate_graph(alignment, alphabet, hmm_list, trans_matrix, emissions_matrix, seq_pos):
    transition_counts = {state: {target: 0 for target in hmm_list} for state in hmm_list}
    emission_counts = {state: {letter: 0 for letter in alphabet} for state in hmm_list}

    for sequence in alignment:
        prev_state = 'S'
        match_index = 0
        for i in range(len(seq_pos)):
            is_match = seq_pos[i][1]
            if is_match:
                match_index += 1
                state = f'D{match_index}' if sequence[i] == '-' else f'M{match_index}'
            else:
                state = f'I{match_index}' if sequence[i] != '-' else None

            if state:
                if state in hmm_list:
                    if state.startswith('M') or state.startswith('I'):
                        if sequence[i] in alphabet:
                            emission_counts[state][sequence[i]] += 1
                    transition_counts[prev_state][state] += 1
                    prev_state = state

        transition_counts[prev_state]['E'] += 1

    for state in hmm_list:
        total_transitions = sum(transition_counts[state].values())
        if total_transitions > 0:
            for target in hmm_list:
                trans_matrix.at[state, target] = transition_counts[state][target] / total_transitions

    for state in hmm_list:
        total_emissions = sum(emission_counts[state].values())
        if total_emissions > 0:
            for letter in alphabet:
                emissions_matrix.at[state, letter] = emission_counts[state][letter] / total_emissions

    return trans_matrix, emissions_matrix


def profile_hmm(threshold: float, alphabet: List[str], alignment: List[str]):
    seq_pos = []
    for i in range(len(alignment[0])):
        pos = [seq[i] for seq in alignment]
        num_dels = sum(1 for letter in pos if letter == '-')
        seq_pos.append((pos, num_dels / len(pos) < threshold))

    alignment_star = [pos[0] for pos in seq_pos if pos[1]]

    hmm_length = len(alignment_star)
    hmm_list = ['S', 'I0'] + [f'{state}{i}' for i in range(1, hmm_length + 1) for state in ['M', 'D', 'I']] + ['E']

    trans_matrix = pd.DataFrame(0.0, columns=hmm_list, index=hmm_list)
    emissions_matrix = pd.DataFrame(0.0, columns=alphabet, index=hmm_list)

    populate_graph(alignment, alphabet, hmm_list, trans_matrix, emissions_matrix, seq_pos)

    order = ["S", "I0"]
    for i in range(1, len(alignment_star)+1):
        order.append(f"M{i}")
        order.append(f"D{i}")
        order.append(f"I{i}")
    order.append("E")

    trans_matrix = trans_matrix.reindex(index=order, columns=order)
    emissions_matrix = emissions_matrix.reindex(index=order)
    trans_matrix = trans_matrix.replace(0.0, 0)
    emissions_matrix = emissions_matrix.replace(0.0, 0)

    return trans_matrix, emissions_matrix

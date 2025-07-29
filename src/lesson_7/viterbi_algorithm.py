"""
This file contains an implementation of the Viterbi algorithm.
"""

from typing import List
import pandas as pd

def prob_hidden_path(pi: str, states: List[str], trans_df: pd.DataFrame):
    """
    Calculates the probability of a hidden path.

    Args:
        pi: The hidden path.
        states: The list of states.
        trans_df: The transition matrix.

    Returns:
        The probability of the hidden path.
    """
    probability = float(1/len(states))
    for i in range(len(pi)):
        curr_symbol = pi[i]
        if i != len(pi)-1:
            next_symbol = pi[i+1]
            added_prob = float(trans_df.loc[curr_symbol, next_symbol])
            probability = probability * added_prob
    return probability

def viterbi_algorithm(x: str, alphabet: List[str], states: List[str],
                      trans_df: pd.DataFrame, emissions_df: pd.DataFrame):
    """
    Implements the Viterbi algorithm.

    Args:
        x: The observed sequence.
        alphabet: The alphabet of the observed sequence.
        states: The list of states.
        trans_df: The transition matrix.
        emissions_df: The emission matrix.

    Returns:
        The most probable hidden path.
    """
    pi = ''
    backtrack_df = pd.DataFrame(1, index=states, columns=list(x)).astype(object)
    viterbi_graph = {state: [0] * len(x) for state in states}
    for j in range(len(x)):
        for curr_state in states:
            prob_emission_given_state = emissions_df.loc[curr_state, x[j]]
            if j == 0:
                viterbi_graph[curr_state][j] = prob_hidden_path(pi, states, trans_df) * prob_emission_given_state
                backtrack_df.loc[curr_state, x[j]] = 'S'
            else:
                max_prob = 0.0
                max_prev_state = states[0]
                for prev_state in states:
                    prob_trans = trans_df.loc[prev_state, curr_state]
                    current_prob = viterbi_graph[prev_state][j - 1] * prob_trans * prob_emission_given_state
                    if current_prob > max_prob:
                        max_prob = current_prob
                        max_prev_state = prev_state
                viterbi_graph[curr_state][j] = max_prob
                backtrack_df.iloc[states.index(curr_state), j] = max_prev_state
    max_prob = 0
    most_probable_state = states[0]
    for state in states:
        if viterbi_graph[state][-1] > max_prob:
            max_prob = viterbi_graph[state][-1]
            most_probable_state = state
    pi = most_probable_state + pi

    current_state = most_probable_state
    for i in range(len(x)-1, 0, -1):
        prev_state = backtrack_df.iloc[states.index(current_state), i]
        pi = prev_state + pi
        current_state = prev_state
        
    return pi

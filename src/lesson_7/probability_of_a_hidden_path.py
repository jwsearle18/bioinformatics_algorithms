"""
This file contains a function to calculate the probability of a hidden path in a hidden Markov model.
"""

from typing import List
import pandas as pd

def prob_hidden_path(pi: str, states: List[str], trans_df: pd.DataFrame):
    """
    Calculates the probability of a hidden path in a hidden Markov model.

    Args:
        pi: The hidden path.
        states: The states of the hidden Markov model.
        trans_df: The transition matrix of the hidden Markov model.

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
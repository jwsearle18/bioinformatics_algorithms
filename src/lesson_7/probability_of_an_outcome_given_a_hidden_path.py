"""
This file contains a function to calculate the probability of an outcome given a hidden path in a hidden Markov model.
"""

from typing import List
import pandas as pd

def prob_outcome_given_hidden_path(x:str, alphabet: List[str], pi: str, states: List[str], emissions_df: pd.DataFrame):
    """
    Calculates the probability of an outcome given a hidden path in a hidden Markov model.

    Args:
        x: The outcome string.
        alphabet: The alphabet of the outcome string.
        pi: The hidden path.
        states: The states of the hidden Markov model.
        emissions_df: The emission matrix of the hidden Markov model.

    Returns:
        The probability of the outcome given the hidden path.
    """
    probability = 1
    for i in range(len(pi)):
        curr_pi = pi[i]
        curr_x = x[i]
        added_prob = float(emissions_df.loc[curr_pi, curr_x])
        probability = probability * added_prob
    return probability
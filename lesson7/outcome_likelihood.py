from typing import List
import pandas as pd # type: ignore

def outcome_likelihood(x: str, alphabet: List[str], states: List[str],
                      trans_df: pd.DataFrame, emissions_df: pd.DataFrame):
    graph = {state: [0] * len(x) for state in states}
    for j in range(len(x)):
        for curr_state in states:
            prob_emission_given_state = emissions_df.loc[curr_state, x[j]]
            if j == 0:
                graph[curr_state][j] = 1/len(states) * prob_emission_given_state
            else:
                total_prob = 0.0
                for prev_state in states:
                    prob_trans = trans_df.loc[prev_state, curr_state]
                    current_prob = graph[prev_state][j - 1] * prob_trans * prob_emission_given_state
                    total_prob += current_prob
                graph[curr_state][j] = total_prob
    
    outcome_likelihood = 0
    for state in states:
        state_likelihood = graph[state][-1]
        outcome_likelihood += state_likelihood
    
    return outcome_likelihood


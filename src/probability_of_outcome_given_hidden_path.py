from typing import List, Set, Dict, Tuple, Optional

from typing import List
import pandas as pd # type: ignore

def prob_outcome_given_hidden_path(x:str, alphabet: List[str], pi: str, states: List[str], emissions_df: pd.DataFrame):
    probability = 1
    for i in range(len(pi)):
        curr_pi = pi[i]
        curr_x = x[i]
        added_prob = float(emissions_df.loc[curr_pi, curr_x])
        probability = probability * added_prob
    return probability

from typing import List, Set, Dict, Tuple, Optional

from typing import List
import pandas as pd # type: ignore

def prob_hidden_path(pi: str, states: List[str], trans_df: pd.DataFrame):
    probability = float(1/len(states))
    for i in range(len(pi)):
        curr_symbol = pi[i]
        if i != len(pi)-1:
            next_symbol = pi[i+1]
            added_prob = float(trans_df.loc[curr_symbol, next_symbol])
            probability = probability * added_prob
    return probability

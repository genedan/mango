"""
Taken from CAS 2005 exam, question 19
"""
import pandas as pd

events = [1, 2, 3]

probs = [.05, .005, .0005]

# return on marginal surplus
y = .15

data_x = pd.DataFrame.from_dict(
    data={
        'event': events,
        'probability': probs,
        'loss': [250, 1000, 6000]
    }
)

data_y = pd.DataFrame.from_dict(
    data={
        'event': events,
        'probability': probs,
        'loss': [60, 300, 1000]
    }
)

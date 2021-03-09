import numpy as np
import pandas as pd


# you can use this table as an example
distr_table = pd.DataFrame({
    'X': [0, 0, 1, 1],
    'Y': [1, 2, 1, 2],
    'pr': [0.3, 0.25, 0.15, 0.3]
})


class CheckIndependence:

    def __init__(self):
        self.version = 1

    def check_independence(self, distr_table: pd.DataFrame):
        # write your solution here
        pass

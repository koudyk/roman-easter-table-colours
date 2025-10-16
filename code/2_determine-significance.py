from pathlib import Path

import numpy as np
import pandas as pd

from lettercombos import list_possible_letter_combinations


null_csv = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "1_95th-percentiles-of-null-distributions.csv"
)
results = pd.read_csv(null_csv, index_col=0)

real_csv = Path(__file__).resolve().parents[1] / "data" / "real-computus-data.csv"
mat_df = pd.read_csv(real_csv)
mat = mat_df.values

patterns = list_possible_letter_combinations(length=3)

concat_pages = mat.T.flatten()
letter_list = [str(letter) for letter in concat_pages]
letter_string = "".join(letter_list)
for pattern in patterns:
    count = int(letter_string.count(pattern))
    results.loc["real_count", pattern] = count


destination = Path(__file__).resolve().parents[1] / "data" / "2_results.csv"
results.to_csv(destination)

d = 1

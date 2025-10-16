from pathlib import Path

import numpy as np
import pandas as pd

from generator import generate_matrix
from lettercombos import list_possible_letter_combinations


n_iterations = 10000
alpha = 0.05

patterns = list_possible_letter_combinations(length=3)
n_patterns = len(patterns)
alpha_corrected = 0.05 / n_patterns
i_nfth_percentile = int(np.ceil(n_iterations * (1 - alpha_corrected)))
print(i_nfth_percentile)

ar = np.zeros(shape=(n_iterations, n_patterns))
df = pd.DataFrame(data=ar, columns=patterns, index=range(n_iterations)).astype(int)

for i_iteration in range(n_iterations):
    mat = generate_matrix()
    concat_pages = mat.T.flatten()
    letter_list = [str(letter) for letter in concat_pages]
    letter_string = "".join(letter_list)
    for pattern in patterns:
        df.loc[i_iteration, pattern] = letter_string.count(pattern)

results = pd.DataFrame(
    columns=patterns, index=["95th_percentile_of_null", "real_count", "difference"]
)

for pattern in patterns:
    col = df[pattern].sort_values().reset_index(drop=True)
    results.loc["95th_percentile_of_null", pattern] = int(col[i_nfth_percentile])

destination = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "1_95th-percentiles-of-null-distributions.csv"
)
results.to_csv(destination, index=True)

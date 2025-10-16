from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
import seaborn as sns

from generator import generate_matrix


cmap = ListedColormap(["tab:red", "tab:green", "tab:blue"])
changes = {
    "R": 1,
    "G": 2,
    "B": 3,
}

n_rows, n_cols = 4, 4
fig, axs = plt.subplots(n_rows, n_cols, figsize=(20, 25))

for i_row in range(n_rows):
    for i_col in range(n_cols):
        mat = generate_matrix()
        df = pd.DataFrame(mat)
        df = df.replace(to_replace=changes)
        sns.heatmap(
            df, cmap=cmap, cbar=False, ax=axs[i_row, i_col], linewidth=0.5, square=True
        )

plt.suptitle("Random matrices")

plt.tight_layout()

destination = (
    Path(__file__).resolve().parents[1]
    / "figures"
    / "0_visualize-random-matrix-generation.png"
)
plt.savefig(destination)

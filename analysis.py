import random

import numpy as np


def generate_matrix(rows=19, cols=16, letters=["R", "B", "G"]):
    matrix = np.empty((rows, cols), dtype=str)

    last_first_letter = random.choice(letters)
    for i_col in range(cols):
        if (i_col + 1) % 2 == 0:
            first_letter = random.choice(letters)
        else:
            first_letter = last_first_letter
        matrix[0, i_col] = first_letter
        last_first_letter = first_letter

        for i_row in range(1, rows):
            # Pick a random letter different from the one above
            options = list(set(letters).difference(set(first_letter)))
            matrix[i_row, i_col] = random.choice(options)

    return matrix


# Example usage:
mat = generate_matrix()
print(mat)

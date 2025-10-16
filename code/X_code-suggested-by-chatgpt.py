import numpy as np
import random

def generate_matrix(rows=19, cols=16, letters=('R', 'B', 'G')):
    matrix = np.empty((rows, cols), dtype=str)
    
    for c in range(cols):
        # Pick a random first letter for the column
        matrix[0, c] = random.choice(letters)
        for r in range(1, rows):
            # Pick a random letter different from the one above
            options = [l for l in letters if l != matrix[r-1, c]]
            matrix[r, c] = random.choice(options)
    
    return matrix

# Example usage:
mat = generate_matrix()
print(mat)

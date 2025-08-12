import numpy as np
import matplotlib.pyplot as plt
import utils

P = np.array(
    [
        [3, 0.75, 0.35, 0.25, 0.85],
        [0.15, 0, 0.35, 0.25, 0.05],
        [0.15, 0.15, 22, 0.25, 0.05],
        [0.15, 0.05, 0.05, 0, 0.05],
        [0.55, 0.05, 0.25, 0.25, 0],
    ]
)

X0 = np.array([[0], [0], [0], [1], [0]])

### START CODE HERE ###

# Multiply matrix P and X_0 (matrix multiplication).
X1 = P @ X0

### END CODE HERE ###

print(f"Sum of columns of P: {sum(P)}")
print(f"X1:\n{X1}")


def center_data(Y):
    """
    Center your original data
    Args:
         Y (ndarray): input data. Shape (n_observations x n_pixels)
    Outputs:
        X (ndarray): centered data
    """
    ### START CODE HERE ###
    mean_vector = np.mean(Y, axis=0)
    mean_matrix = np.repeat(mean_vector, Y.size)
    # use np.reshape to reshape into a matrix with the same size as Y. Remember to use order='F'
    ##mean_matrix =

    X = Y - mean_matrix
    ### END CODE HERE ###
    return X


center_data(P)

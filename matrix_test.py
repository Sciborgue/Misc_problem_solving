import numpy as np
import matplotlib.pyplot as plt
import utils
import scipy.sparse.linalg
from numpy.linalg import eig

n_array = np.array([[1, 2, 1], [2, 1, 1], [-1, 2, 1]])

# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)

# calculating the determinant of matrix
det = np.linalg.det(n_array)

print("\nDeterminant of given 2X2 matrix:")
print(int(det))

A = np.array([[3, -9], [2, 4]])
b = np.array([-42, 2])
z = np.linalg.solve(A, b)
print(z)

M = np.array([[1, 2, 3], [2, 6, 12], [4, -8, 4]])
c = np.array([10, 4, 8])
y = np.linalg.solve(M, c)
print(y)

N = np.array([[2, 1, 5], [1, 3, 1], [3, 4, 6]])

print(np.linalg.matrix_rank(N))


def swap_rows(M, row_index_1, row_index_2):
    """
    Swap rows in the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to perform row swaps on.
    - row_index_1 (int): Index of the first row to be swapped.
    - row_index_2 (int): Index of the second row to be swapped.
    """

    # Copy matrix M so the changes do not affect the original matrix.
    M = M.copy()
    # Swap indexes
    M[[row_index_1, row_index_2]] = M[[row_index_2, row_index_1]]
    return M


def get_index_first_non_zero_value_from_column(M, column, starting_row):
    """
    Retrieve the index of the first non-zero value in a specified column of the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to search for non-zero values.
    - column (int): The index of the column to search.
    - starting_row (int): The starting row index for the search.

    Returns:
    int: The index of the first non-zero value in the specified column, starting from the given row.
                Returns -1 if no non-zero value is found.
    """
    # Get the column array starting from the specified row
    column_array = M[starting_row:, column]
    for i, val in enumerate(column_array):
        # Iterate over every value in the column array.
        # To check for non-zero values, you must always use np.isclose instead of doing "val == 0".
        if not np.isclose(val, 0, atol=1e-5):
            # If one non zero value is found, then adjust the index to match the correct index in the matrix and return it.
            index = i + starting_row
            return index
    # If no non-zero value is found below it, return -1.
    return -1


def get_index_first_non_zero_value_from_row(M, row, augmented=False):
    """
    Find the index of the first non-zero value in the specified row of the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to search for non-zero values.
    - row (int): The index of the row to search.
    - augmented (bool): Pass this True if you are dealing with an augmented matrix,
                        so it will ignore the constant values (the last column in the augmented matrix).

    Returns:
    int: The index of the first non-zero value in the specified row.
                Returns -1 if no non-zero value is found.
    """

    # Create a copy to avoid modifying the original matrix
    M = M.copy()

    # If it is an augmented matrix, then ignore the constant values
    if augmented == True:
        # Isolating the coefficient matrix (removing the constant terms)
        M = M[:, :-1]

    # Get the desired row
    row_array = M[row]
    for i, val in enumerate(row_array):
        # If finds a non zero value, returns the index. Otherwise returns -1.
        if not np.isclose(val, 0, atol=1e-5):
            return i
    return -1


def augmented_matrix(A, B):
    """
    Create an augmented matrix by horizontally stacking two matrices A and B.

    Parameters:
    - A (numpy.array): First matrix.
    - B (numpy.array): Second matrix.

    Returns:
    - numpy.array: Augmented matrix obtained by horizontally stacking A and B.
    """
    augmented_M = np.hstack((A, B))
    return augmented_M


def row_echelon_form(A, B):
    """
    Utilizes elementary row operations to transform a given set of matrices,
    which represent the coefficients and constant terms of a linear system, into row echelon form.

    Parameters:
    - A (numpy.array): The input square matrix of coefficients.
    - B (numpy.array): The input column matrix of constant terms

    Returns:
    numpy.array: A new augmented matrix in row echelon form with pivots as 1.
    """

    # Before any computation, check if matrix A (coefficient matrix) has non-zero determinant.
    # It will be used the numpy sub library np.linalg to compute it.

    det_A = np.linalg.det(A)

    # Returns "Singular system" if determinant is zero
    if np.isclose(det_A, 0) == True:
        return "Singular system"

    # Make copies of the input matrices to avoid modifying the originals
    A = A.copy()
    B = B.copy()

    # Convert matrices to float to prevent integer division
    A = A.astype("float64")
    B = B.astype("float64")

    # Number of rows in the coefficient matrix
    num_rows = len(A)

    ### START CODE HERE ###

    # Transform matrices A and B into the augmented matrix M
    M = augmented_matrix(A, B)

    # Iterate over the rows.
    for row in range(num_rows):

        # The first pivot candidate is always in the main diagonal, let's get it.
        # Remember that the diagonal elements in a matrix has the same index for row and column.
        # You may access a matrix value by typing M[row, column]. In this case, column = None
        pivot_candidate = M[row, row]

        # If pivot_candidate is zero, it cannot be a pivot for this row.
        # So the first step you need to take is to look at the rows below it to check if there is a non-zero element in the same column.
        # The usage of np.isclose is a good practice when comparing two floats.
        if np.isclose(pivot_candidate, 0) == True:
            # Get the index of the first non-zero value below the pivot_candidate.
            first_non_zero_value_below_pivot_candidate = (
                get_index_first_non_zero_value_from_column(M, row, row)
            )

            # Swap rows
            M = swap_rows(M, row, first_non_zero_value_below_pivot_candidate)

            # Get the pivot, which is in the main diagonal now
            pivot = M[row, row]

        # If pivot_candidate is already non-zero, then it is the pivot for this row
        else:
            pivot = pivot_candidate

        # Now you are ready to apply the row reduction in every row below the current

        # Divide the current row by the pivot, so the new pivot will be 1. You may use the formula current_row -> 1/pivot * current_row
        # Where current_row can be accessed using M[row].
        M[row] = 1 / pivot * M[row]

        # Perform row reduction for rows below the current row
        for j in range(row + 1, num_rows):
            # Get the value in the row that is below the pivot value.
            # Remember that, since you are dealing only with non-singular matrices, the pivot is in the main diagonal.
            # Therefore, the values in row j that are below the pivot, must have column index the same index as the column index for the pivot.
            value_below_pivot = M[row + 1, row]

            # Perform row reduction using the formula:
            # row_to_reduce -> row_to_reduce - value_below_pivot * pivot_row
            M[j] = M[j] - value_below_pivot * M[row]

    ### END CODE HERE ###

    return M


A = np.array([[1, 2, 3], [0, 1, 0], [0, 0, 5]])
B = np.array([[1], [2], [4]])
M1 = row_echelon_form(A, B)
print(M1)


def back_substitution(M):
    """
    Perform back substitution on an augmented matrix (with unique solution) in reduced row echelon form to find the solution to the linear system.

    Parameters:
    - M (numpy.array): The augmented matrix in row echelon form with unitary pivots (n x n+1).

    Returns:
    numpy.array: The solution vector of the linear system.
    """

    # Make a copy of the input matrix to avoid modifying the original
    M = M.copy()

    # Get the number of rows (and columns) in the matrix of coefficients
    num_rows = M.shape[0]

    ### START CODE HERE ####

    # Iterate from bottom to top
    for row in reversed(range(num_rows)):
        substitution_row = M[row]

        # Get the index of the first non-zero element in the substitution row. Remember to pass the correct value to the argument augmented.
        index = get_index_first_non_zero_value_from_row(M, row, augmented=True)

        # Iterate over the rows above the substitution_row
        for j in range(row):

            # Get the row to be reduced. The indexing here is similar as above, with the row variable replaced by the j variable.
            row_to_reduce = M[j]

            # Get the value of the element at the found index in the row to reduce
            value = row_to_reduce[index]

            # Perform the back substitution step using the formula row_to_reduce -> row_to_reduce - value * substitution_row
            row_to_reduce = row_to_reduce - value * substitution_row

            # Replace the updated row in the matrix, be careful with indexing!
            M[j, :] = row_to_reduce

    ### END CODE HERE ####

    # Extract the solution from the last column
    solution = M[:, -1]

    return solution


M2 = back_substitution(M1)
print(M2)


def gaussian_elimination(A, B):
    """
    Solve a linear system represented by an augmented matrix using the Gaussian elimination method.

    Parameters:
    - A (numpy.array): Square matrix of size n x n representing the coefficients of the linear system
    - B (numpy.array): Column matrix of size 1 x n representing the constant terms.

    Returns:
    numpy.array or str: The solution vector if a unique solution exists, or a string indicating the type of solution.
    """

    ### START CODE HERE ###

    # Get the matrix in row echelon form
    row_echelon_M = row_echelon_form(A, B)

    # If the system is non-singular, then perform back substitution to get the result.
    # Since the function row_echelon_form returns a string if there is no solution, let's check for that.
    # The function isinstance checks if the first argument has the type as the second argument, returning True if it does and False otherwise.
    if not isinstance(row_echelon_M, str):
        solution = back_substitution(row_echelon_M)

    ### END SOLUTION HERE ###

    return solution


# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = -12
c = 11

# calculate the discriminant
d = (b**2) - (4 * a * c)

# find two solutions
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print("The solution are {0} and {1}".format(sol1, sol2))

K = np.array([[3, 2], [5, 8]])
w, v = eig(K)
print("E-value:", w)
print("E-vector", v)
print("Cov_matrix is", np.cov(K))

a2 = np.array([[800, 40, 0], [40, 2, 0], [0, 0, 0]])
w, v = eig(a2)
print("E-value:", w)
print("E-vector", v)
print("Cov_matrix is", np.cov(a2))

m3 = np.array([[1, 2, 4], [3, -1, 5], [-4, -3, -11]])

rank3 = np.linalg.matrix_rank(m3)
print("rang de m3:", rank3)

m4 = np.array([[1, 0, 1], [0, 1, 0], [1, 1, 1]])

m5 = np.array([[2, 8, 7], [4, 3, 9], [1, 9, 5]])

det34 = np.linalg.det(m4) * np.linalg.det(m5)
print(det34)

m6 = np.array([[2, 3, 1], [0, -1, 2], [-1, 1, 4]])

det6 = np.linalg.det(m6)

print(det6)

m7 = np.array([[2, 1], [-3, 6]])

poly7 = np.poly(m7)

print(poly7)


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
    mean_matrix = np.repeat(mean_vector, len(Y))
    # use np.reshape to reshape into a matrix with the same size as Y. Remember to use order='F'
    mean_matrix = mean_matrix.reshape(len(Y), len(Y[0]), order="F")

    X = Y - mean_matrix
    ### END CODE HERE ###
    return X


def get_cov_matrix(X):
    """Calculate covariance matrix from centered data X
    Args:
        X (np.ndarray): centered data matrix
    Outputs:
        cov_matrix (np.ndarray): covariance matrix
    """

    ### START CODE HERE ###
    cov_matrix = 1 / (len(X) - 1) * np.dot(np.matrix.transpose(X), X)
    ### END CODE HERE ###

    return cov_matrix


# GRADED cell
def perform_PCA(X, eigenvecs, k):
    """
    Perform dimensionality reduction with PCA
    Inputs:
        X (ndarray): original data matrix. Has dimensions (n_observations)x(n_variables)
        eigenvecs (ndarray): matrix of eigenvectors. Each column is one eigenvector. The k-th eigenvector
                            is associated to the k-th eigenvalue
        k (int): number of principal components to use
    Returns:
        Xred
    """

    ### START CODE HERE ###
    V = (eigenvectors / np.mean(eigenvectors, axis=0))[0:2]
    Xred = center_data(X)
    Xred = Xred @ np.matrix.transpose(V)

    ### END CODE HERE ###
    return Xred


m = np.arange(10, 100, 10)  # array [10, 20, 30, 40, 50, 60, 70, 80, 90]
m = m.reshape(3, 3)
center_data_m = center_data(m)


cov_matrix = get_cov_matrix(center_data_m)
eigenvalues, eigenvectors = np.linalg.eig(m)
print(eigenvectors.shape)
Eig_mean = np.mean(eigenvectors, axis=0)
Eig_normalized = (eigenvectors / Eig_mean)[0:2]
print(Eig_mean, Eig_normalized)

print(perform_PCA(m, eigenvectors, 2))

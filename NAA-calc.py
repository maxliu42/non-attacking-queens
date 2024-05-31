import itertools

import numpy as np

# check if a given arrangement is an NAA for bishops
def is_bishop_naa(mat):
    # check that the diagonals contain at most one bishop
    diagonals = [mat.diagonal(i) for i in range(-mat.shape[0]+1, mat.shape[1])]
    anti_diagonals = [mat[::-1,:].diagonal(i)
                      for i in range(-mat.shape[0]+1, mat.shape[1])]

    for diagonal in diagonals + anti_diagonals:
        if np.sum(diagonal) > 1:
            return False

    return True


def is_rook_naa(mat):
    # check that each row and column contains at most one rook
    for i in range(mat.shape[0]):
        # if there is more than one rook in a row
        if np.sum(mat[i, :]) > 1:
            return False
        # if there is more than one rook in a column
        if np.sum(mat[:, i]) > 1:
            return False
    return True


def is_queen_naa(mat):
    # check for both rook and bishop non-attacking arrangements
    # because a queen moves like a rook and bishop combined
    return is_rook_naa(mat) and is_bishop_naa(mat)

# check all square boards from 1 to 8
for size in range(1, 9):
    bishop_naas = 0
    rook_naas = 0
    queen_naas = 0

    # set dimensions
    N = size
    M = size
    K = size

    # generate all possible positions for bishops
    positions = list(itertools.product(range(M), range(N)))

    # generate all possible arrangements of k bishops
    combinations = list(itertools.combinations(positions, K))

    count = 0
    for combination in combinations:
        # create a matrix representation of the arrangement
        mat = np.zeros((M, N), dtype=int)
        for row, col in combination:
            mat[row, col] = 1

        # check if the arrangement is a non-attacking arrangement
        if is_bishop_naa(mat):
            bishop_naas += 1
        if is_rook_naa(mat):
            rook_naas += 1
        if is_queen_naa(mat):
            queen_naas += 1

    print("N={n}, M={m}, K={k}".format(n=N, m=M, k=K))
    print("-------------------")
    print("Bishop NAAs: {}".format(bishop_naas))
    print("Rook NAAs: {}".format(rook_naas))
    print("Queen NAAs: {}".format(queen_naas))
    print(" ")

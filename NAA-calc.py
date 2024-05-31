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


def is_unique_solution(mat, fundamental_solutions):
    # check if the current solution is a rotation or reflection of any previously found solution
    for solution in fundamental_solutions:
        if np.array_equal(mat, solution):
            return False
        if np.array_equal(mat, np.rot90(solution)):
            return False
        if np.array_equal(mat, np.rot90(solution, 2)):
            return False
        if np.array_equal(mat, np.rot90(solution, 3)):
            return False
        if np.array_equal(mat, np.fliplr(solution)):
            return False
        if np.array_equal(mat, np.flipud(solution)):
            return False
        if np.array_equal(mat, np.fliplr(np.rot90(solution))):
            return False
        if np.array_equal(mat, np.flipud(np.rot90(solution))):
            return False
    return True


# check all square boards from 1 to 8
for size in range(1, 11):
    bishop_naas = 0
    rook_naas = 0
    queen_naas = 0
    fundamental_solutions = []

    # set dimensions
    N = size
    M = size
    K = size

    # generate all possible permutations of row indices
    row_permutations = list(itertools.permutations(range(M)))

    count = 0
    for perm in row_permutations:
        # create a matrix representation of the arrangement
        mat = np.zeros((M, N), dtype=int)
        for row, col in enumerate(perm):
            mat[row, col] = 1

        # check if the arrangement is a non-attacking arrangement
        # if is_bishop_naa(mat):
        #     bishop_naas += 1
        # if is_rook_naa(mat):
        #     rook_naas += 1
        if is_queen_naa(mat):
            queen_naas += 1
            if is_unique_solution(mat, fundamental_solutions):
                fundamental_solutions.append(mat)

    print("N={n}, M={m}, K={k}".format(n=N, m=M, k=K))
    print("-------------------")
    # print("Bishop NAAs: {}".format(bishop_naas))
    # print("Rook NAAs: {}".format(rook_naas))
    print("Queen NAAs: {}".format(queen_naas))
    print("Fundamental Solutions: {}".format(len(fundamental_solutions)))
    print(" ")

def solve_n_queens(N):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row, -1, -1), range(col, N)):
            if board[i][j] == 'Q':
                return False

        return True

    def backtrack(board, row):
        if row == N:
            solutions.append(["".join(row) for row in board])
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'

    solutions = []
    empty_board = [['.' for _ in range(N)] for _ in range(N)]
    backtrack(empty_board, 0)
    return solutions

def print_solutions(solutions):
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in solution:
            print(row)
        print("\n")
N = 4 
solutions = solve_n_queens(N)
print_solutions(solutions)

"""
Explanation of the Backtracking Approach:

The is_safe function checks whether it's safe to place a queen at a given row and column. It ensures no queens threaten each other by checking the same column and both diagonal directions.

The backtrack function recursively explores all possible queen placements on the board row by row. If it reaches the Nth row without conflicts, it records the solution.

We start with an empty board of size N×N and initiate the backtracking process from the first row (row 0).

The solve_n_queens function collects all the solutions found during backtracking and returns them.

We print the solutions as chessboard representations, using 'Q' for queens and '.' for empty squares.

Time Complexity Analysis:

The time complexity of this backtracking algorithm depends on the number of recursive calls and the work done in each call. In the worst case, it explores all possible combinations of queen placements, leading to an exponential time complexity of O(N!). This makes the algorithm inefficient for larger values of N.
"""

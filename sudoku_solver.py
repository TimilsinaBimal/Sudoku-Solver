class SudokuSolver:
    def __init__(self, board):
        self.board = board
        self.n = len(self.board[0])

    def find_empty_position(self):
        """
            Returns the positions(row, col) of empty cells i.e cells to be filled.
        """
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def is_valid(self, num, pos: tuple):
        """
        Checks if the number we are about to fill is valid or not in that position.
        """
        row, col = pos
        # Check Row
        if num in self.board[row]:
            return False

        # Check column
        colum_vals = [self.board[idx][col] for idx in range(self.n)]
        if num in colum_vals:
            return False

        # Check 3*3 Grid
        start_x = (row // 3) * 3
        start_y = (col // 3) * 3

        box_vals = [self.board[row][col] for col in range(
            start_y, start_y+3) for row in range(start_x, start_x+3)]

        if num in box_vals:
            return False

        return True

    def solve(self):
        """
        Solves the Sudoku recusively, if sudoku cannot be solved returns False
        """
        pos = self.find_empty_position()
        if not pos:
            return True  # Board already solved
        else:
            row, col = pos

        for num in range(1, 10):
            if self.is_valid(num, pos):
                self.board[row][col] = num

                # if the newly added value helps to solve the problem, solve it
                if self.solve():
                    return True

                # if after adding the board is not solved, reset that value and go back
                self.board[row][col] = 0
        return False

    def print_board(self):
        """
        Prints the board.
        """
        print("+" + "---+" * self.n)
        for i, row in enumerate(board):
            print(("|" + " {}   {}   {} |" * 3).format(*
                                                       [x for x in row]))
            if i % 3 == 2:
                print("+" + "---+" * self.n)
            else:
                print("+" + "   +" * self.n)


if __name__ == "__main__":
    # board = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
    #          [6, 8, 0, 0, 7, 0, 0, 9, 0],
    #          [1, 9, 0, 0, 0, 4, 5, 0, 0],
    #          [8, 2, 0, 1, 0, 0, 0, 4, 0],
    #          [3, 0, 4, 6, 0, 2, 9, 0, 0],
    #          [0, 5, 0, 0, 0, 3, 0, 2, 8],
    #          [0, 0, 9, 3, 0, 0, 0, 7, 4],
    #          [0, 4, 0, 0, 5, 0, 0, 3, 6],
    #          [7, 0, 3, 0, 1, 8, 0, 0, 0]]

    board = [[0, 1, 0, 7, 0, 0, 0, 2, 4],
             [0, 0, 2, 1, 3, 5, 0, 0, 7],
             [0, 0, 0, 0, 4, 2, 0, 0, 0],
             [0, 6, 4, 0, 7, 0, 0, 0, 9],
             [9, 0, 1, 0, 0, 6, 4, 0, 8],
             [8, 3, 7, 0, 1, 4, 0, 6, 0],
             [0, 0, 6, 0, 0, 1, 9, 0, 0],
             [2, 0, 3, 4, 8, 7, 0, 5, 6],
             [1, 0, 5, 6, 0, 0, 7, 0, 2]]
    solver = SudokuSolver(board)
    solver.solve()
    solver.print_board()

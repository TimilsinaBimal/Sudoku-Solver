from sudoku_solver import SudokuSolver
import unittest


class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.board = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
                      [6, 8, 0, 0, 7, 0, 0, 9, 0],
                      [1, 9, 0, 0, 0, 4, 5, 0, 0],
                      [8, 2, 0, 1, 0, 0, 0, 4, 0],
                      [3, 0, 4, 6, 0, 2, 9, 0, 0],
                      [0, 5, 0, 0, 0, 3, 0, 2, 8],
                      [0, 0, 9, 3, 0, 0, 0, 7, 4],
                      [0, 4, 0, 0, 5, 0, 0, 3, 6],
                      [7, 0, 3, 0, 1, 8, 0, 0, 0]]
        self.solver = SudokuSolver(self.board)
        self.solver.solve()
        self.result = [i for i in range(1, 10)]

    def test_row(self):
        """
        Checks if every row contains value from 1 to 9 or not. Also checks if there are any duplicate items or not.
        """
        for i in range(len(self.solver.board[0])):
            self.assertListEqual(sorted(self.solver.board[i]), self.result)

    def test_column(self):
        """
        Checks if every column contains value from 1 to 9 or not. Also checks if there are any duplicate items or not.
        """
        for i in range(len(self.solver.board[0])):
            res = [self.solver.board[j][i] for j in range(9)]
            self.assertListEqual(sorted(res), self.result)

    def test_box(self):
        """
        Checks if every 3*3 box contains value from 1 to 9 or not. Also checks if there are any duplicate items or not.
        """
        for row in range(3):
            for col in range(3):
                start_x = row * 3
                start_y = col * 3
                vals = [self.solver.board[row][col] for col in range(
                    start_y, start_y+3) for row in range(start_x, start_x+3)]
                self.assertListEqual(sorted(vals), self.result)


if __name__ == "__main__":
    unittest.main()

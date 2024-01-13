import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        for row in range(1, 20):
            for col in range(1, 20):
                with self.subTest(col=col, row=row):
                    maze = Maze(0,0, row, col, 10, 10)
                    self.assertEqual(len(maze.cells), row)
                    self.assertEqual(len(maze.cells[0]), col)

if __name__ == "__main__":
    unittest.main()
        
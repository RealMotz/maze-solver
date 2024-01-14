import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        for row in range(1, 20):
            for col in range(1, 20):
                with self.subTest(col=col, row=row):
                    maze = Maze(0, 0, row, col, 10, 10)
                    self.assertEqual(len(maze.cells), row)
                    self.assertEqual(len(maze.cells[0]), col)
    
    def test_maze_break_entrace_and_exit(self):
        row = 10
        col = 10
        maze = Maze(0, 0, row, col, 10, 10)
        maze.break_entrance_and_exit()

        self.assertEqual(maze.cells[0][0].has_left_wall, False)
        self.assertEqual(maze.cells[row-1][col-1].has_right_wall, False)

    def test_maze_break_right_wall(self):
        row = 10
        col = 10
        maze = Maze(0, 0, row, col, 10, 10)
        maze.break_wall(0, 0, 0, 1)
        self.assertEqual(maze.cells[0][0].has_right_wall, False)

    def test_maze_break_left_wall(self):
        row = 10
        col = 10
        maze = Maze(0, 0, row, col, 10, 10)
        maze.break_wall(1, 1, 1, 0)
        self.assertEqual(maze.cells[1][1].has_left_wall, False)

    def test_maze_break_top_wall(self):
        row = 10
        col = 10
        maze = Maze(0, 0, row, col, 10, 10)
        maze.break_wall(1, 1, 0, 1)
        self.assertEqual(maze.cells[1][1].has_top_wall, False)

    def test_maze_break_bottom_wall(self):
        row = 10
        col = 10
        maze = Maze(0, 0, row, col, 10, 10)
        maze.break_wall(1, 1, 2, 1)
        self.assertEqual(maze.cells[1][1].has_bottom_wall, False)

    def test_maze_reset_cells_visited(self):
        row = 10
        col = 10
        maze = Maze(0, 0, row, col, 10, 10)
        maze.break_entrance_and_exit()
        maze.break_walls()
        maze.reset_cells_visited()
        for n in range(row):
            for m in range(col):
                self.assertEqual(maze.cells[n][m].visited, False)

if __name__ == "__main__":
    unittest.main()

import random
from util import Cell, Point
from time import sleep


class Maze:
    """
    Maze builder class

    Args:
        x1 (int): Starting x position of the maze matrix
        y1 (int): Starting y position of the maze matrix
        num_rows (int): Number of rows
        num_cols (int): Number of columns
        cell_size_x (int): Width of each cell
        cell_size_y (int): Height of each cell
        seed (int): Optional seed value
        window (Window): Optional reference to the window class
    """
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, seed=None, window=None
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.directions = [(0,1), (1,0), (0,-1), (-1,0)]
        random.seed(seed)
        self.create_cells()

    def create_cells(self) -> None:
        self.cells = []
        for row in range(self.num_rows):
            new_list = []
            for col in range(self.num_cols):
                x = self.x1 + col * self.cell_size_x
                y = self.y1 + row * self.cell_size_y

                new_cell = Cell(
                    Point(x, y),
                    Point(x + self.cell_size_x, y + self.cell_size_y),
                    self.window,
                )
                new_list.append(new_cell)
                self.draw_cell(new_cell)

            self.cells.append(new_list)

    def draw_cell(self, cell) -> None:
        cell.draw("black")
        self.animate()

    def animate(self) -> None:
        if self.window is None:
            return
        self.window.redraw()
        sleep(0.03)

    def break_entrance_and_exit(self) -> None:
        top_left_cell = self.cells[0][0]
        top_left_cell.has_left_wall = False
        self.draw_cell(self.cells[0][0])

        bottom_left_cell = self.cells[self.num_rows-1][self.num_cols-1]
        bottom_left_cell.has_right_wall = False
        self.draw_cell(bottom_left_cell)

    def break_walls(self) -> None:
        self.dfs(0, 0)

    def dfs(self, i, j) -> None:
        for move in random.sample(self.directions, len(self.directions)):
            row = i + move[0]
            col = j + move[1]
            self.cells[i][j].visited = True
            if(row >= 0 and row < len(self.cells) and col >= 0 and col < len(self.cells[0]) and not self.cells[row][col].visited):
                self.break_wall(i, j, row, col)
                self.draw_cell(self.cells[i][j])
                self.dfs(row, col)

    def break_wall(self, x1, y1, x2, y2) -> None:
        # If we moved right
        if(y2 - y1 == 1):
            self.cells[x1][y1].has_right_wall = False
            self.cells[x2][y2].has_left_wall = False
            return
        # If we moved left
        if(y2 - y1 == -1):
            self.cells[x1][y1].has_left_wall = False
            self.cells[x2][y2].has_right_wall = False
            return
        # If we moved down
        if(x2 - x1 == 1):
            self.cells[x1][y1].has_bottom_wall = False
            self.cells[x2][y2].has_top_wall = False
            return
        # If we moved up
        if(x2 - x1 == -1):
            self.cells[x1][y1].has_top_wall = False
            self.cells[x2][y2].has_bottom_wall = False
            return

    def reset_cells_visited(self) -> None:
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.cells[row][col].visited = False

    def solve(self) -> bool:
        self.solve_dfs(0, 0)

    def solve_dfs(self, i, j) -> bool:
        if(i == self.num_rows-1 and j == self.num_cols-1):
            return True

        for direction in self.directions:
            row = i + direction[0]
            col = j + direction[1]
            self.cells[i][j].visited = True
            if(0 <= row < len(self.cells) and 0 <= col < len(self.cells[0]) and not self.cells[row][col].visited and self.can_move(self.cells[i][j], direction)):
                self.cells[i][j].draw_move(self.cells[row][col])
                self.animate()
                if (self.solve_dfs(row, col)):
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[row][col], True)
                    self.animate()
                
        return False

    def can_move(self, cell, direction) -> bool:
        if direction == (0,1):
            return not cell.has_right_wall
        elif direction == (1,0):
            return not cell.has_bottom_wall
        elif direction == (0,-1):
            return not cell.has_left_wall
        else:
            return not cell.has_top_wall
            

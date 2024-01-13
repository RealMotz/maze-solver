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
        window (Window): Optional reference to the window class
    """
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.create_cells()

    def create_cells(self):
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

    def draw_cell(self, cell):
        cell.draw("black")
        self.animate()

    def animate(self):
        if self.window is None:
            return

        self.window.redraw()
        sleep(0.05)

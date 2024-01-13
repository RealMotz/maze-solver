from tkinter import Tk, BOTH, Canvas


class Window:
    """
    Handles the creation and destruction of a Tkinter window

    Args:
        width (int): Width of the Tkinter window
        height (int): Height of the Tkinter window
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title = "Maze Solver"
        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False

    def redraw(self):
        # We redraw for reactivity
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


class Point:
    """
    Represents a 2D point inside a Tkinter window

    Args:
        x (int): x coordinate inside a Tkinter window
        y (int): y coordinate inside a Tkinter window
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    """
    Given two points, draws a line between them

    Args:
        p1 (Point): Top-left point inside a Tkinter window
        p2 (Point): bottom-right point inside a Tkinter window
    """
    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=2,
        )
        canvas.pack(fill=BOTH, expand=1)


class Cell:
    """
    Represents a cell inside a window

    Args:
        p1 (Point): Top-left point inside a Tkinter window
        p2 (Point): bottom-right point inside a Tkinter window
        window (Window): Optional reference to the window class
    """
    def __init__(self, p1, p2, window=None):
        self.p1 = p1
        self.p2 = p2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.window = window

    def draw(self, fill_color):
        if self.window is None:
            return

        top_right = Point(self.p2.x, self.p1.y)
        bottom_left = Point(self.p1.x, self.p2.y)

        top_line = Line(self.p1, top_right)
        bottom_line = Line(bottom_left, self.p2)
        left_line = Line(self.p1, bottom_left)
        right_line = Line(top_right, self.p2)

        if self.has_top_wall:
            self.window.draw_line(top_line, fill_color)
        if self.has_left_wall:
            self.window.draw_line(left_line, fill_color)
        if self.has_bottom_wall:
            self.window.draw_line(bottom_line, fill_color)
        if self.has_right_wall:
            self.window.draw_line(right_line, fill_color)

    def draw_move(self, to_cell, undo=False):
        x1 = (self.p1.x + self.p2.x) / 2
        y1 = (self.p1.y + self.p2.y) / 2
        center1 = Point(x1, y1)

        x2 = (to_cell.p1.x + to_cell.p2.x) / 2
        y2 = (to_cell.p1.y + to_cell.p2.y) / 2
        center2 = Point(x2, y2)

        fill_color = "gray" if undo else "red"
        self.window.draw_line(Line(center1, center2), fill_color)

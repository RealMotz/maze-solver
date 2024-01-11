from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title = "Maze Solver"
        self.canvas = Canvas(self.__root)
        self.canvas.pack()
        self.running = False

    def redraw(self):
        # We redraw for reactivity
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.running = True
        while (self.running):
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
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
            width=2
        )
        canvas.pack()


class Cell:
    def __init__(self, p1, p2, window):
        self.p1 = p1
        self.p2 = p2
        self.has_left_wall = False
        self.has_right_wall = False
        self.has_top_wall = False
        self.has_bottom_wall = False
        self.window = window

    def draw(self, fill_color):
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


window = Window(400, 600)
p1 = Point(0, 0)
p2 = Point(10, 10)
# window.draw_line(Line(p1, p2), "red")
c1 = Cell(Point(10, 10), Point(30, 30), window)
c1.has_bottom_wall = True
c1.has_top_wall = True

c1.draw("black")
window.wait_for_close()
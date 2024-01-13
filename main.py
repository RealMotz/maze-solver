from maze import Maze
from util import Window, Point, Cell


def test():
    window = Window(400, 600)
    c1 = Cell(Point(50, 50), Point(100, 100), window)
    c1.has_right_wall = False
    c1.draw("black")

    c2 = Cell(Point(100, 50), Point(150, 100), window)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw("black")

    c3 = Cell(Point(100, 100), Point(150, 150), window)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw("black")

    c4 = Cell(Point(150, 100), Point(200, 150), window)
    c4.has_left_wall = False
    c4.draw("black")

    c1.draw_move(c2)
    c2.draw_move(c3)
    c3.draw_move(c4, True)


def main():
    x1 = 50
    y1 = 50
    rows = 12
    cols = 16
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * x1) / cols
    cell_size_y = (screen_y - 2 * y1) / rows

    window = Window(screen_x, screen_y)
    Maze(x1, y1, rows, cols, cell_size_x, cell_size_y, window)
    window.wait_for_close()


main()

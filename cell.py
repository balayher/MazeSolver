from graphics import Line, Point

class Cell():
    def __init__(self, window=None):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)
        if self.left_wall:
            self._win.draw_line(Line(top_left, bottom_left))
        else:
            self._win.draw_line(Line(top_left, bottom_left), fill_color="black")
        if self.top_wall:
            self._win.draw_line(Line(top_left, top_right))
        else:
            self._win.draw_line(Line(top_left, top_right), fill_color="black")
        if self.right_wall:
            self._win.draw_line(Line(top_right, bottom_right))
        else:
            self._win.draw_line(Line(top_right, bottom_right), fill_color="black")
        if self.bottom_wall:
            self._win.draw_line(Line(bottom_left, bottom_right))
        else:
            self._win.draw_line(Line(bottom_left, bottom_right), fill_color="black")

    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "red"
        else:
            fill_color = "green"
        center1 = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        center2 = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        self._win.draw_line(Line(center1, center2), fill_color)

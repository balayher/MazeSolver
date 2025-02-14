from graphics import Line, Point

class Cell():
    def __init__(self, window, left=True, right=True, top=True, bottom=True):
        self.left_wall = left
        self.right_wall = right
        self.top_wall = top
        self.bottom_wall = bottom
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = window

    def draw(self, x1, y1, x2, y2, fill_color="white"):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)
        if self.left_wall:
            self.__win.draw_line(Line(top_left, bottom_left), fill_color)
        if self.top_wall:
            self.__win.draw_line(Line(top_left, top_right), fill_color)
        if self.right_wall:
            self.__win.draw_line(Line(top_right, bottom_right), fill_color)
        if self.bottom_wall:
            self.__win.draw_line(Line(bottom_left, bottom_right), fill_color)

    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "red"
        else:
            fill_color = "green"
        center1 = Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)
        center2 = Point((to_cell.__x1 + to_cell.__x2) / 2, (to_cell.__y1 + to_cell.__y2) / 2)
        self.__win.draw_line(Line(center1, center2), fill_color)
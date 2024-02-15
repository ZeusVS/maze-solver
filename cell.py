from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None 
        self._y1 = None 
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        if self.has_left_wall:
            self._win.draw_line(left_wall)
        else:
            self._win.draw_line(left_wall, "white")

        right_wall = Line(Point(self._x2, self._y1),Point(self._x2, self._y2))
        if self.has_right_wall:
            self._win.draw_line(right_wall)
        else:
            self._win.draw_line(right_wall, "white")

        top_wall = Line(Point(self._x1, self._y1),Point(self._x2, self._y1))
        if self.has_top_wall:
            self._win.draw_line(top_wall)
        else:
            self._win.draw_line(top_wall, "white")

        bottom_wall = Line(Point(self._x1, self._y2),Point(self._x2, self._y2))
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall)
        else:
            self._win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"

        point1 = Point(((self._x1+self._x2)/2), ((self._y1+self._y2)/2))
        point2 = Point((to_cell._x1+to_cell._x2)/2, (to_cell._y1+to_cell._y2)/2)
        path = Line(point1, point2)
        if self._win:
            self._win.draw_line(path, fill_color)


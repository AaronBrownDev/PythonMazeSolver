from display import Window, Line, Point

class Cell():
    
    def __init__(self, win) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        
        
    def draw(self, x1, y1, x2, y2,):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line=left_wall, fill_color="black")
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line=bottom_wall, fill_color="black")
        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y2), Point(self._x2, self._y1))
            self._win.draw_line(line=right_wall, fill_color="black")
        if self.has_top_wall:
            top_wall = Line(Point(self._x2, self._y1), Point(self._x1, self._y1))
            self._win.draw_line(line=top_wall, fill_color="black")
        
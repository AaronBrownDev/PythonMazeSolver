from display import Window, Line, Point

class Cell():
    
    def __init__(self, win : Window) -> None:
        self.visited = False
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
            fill_color = "black"
        else:
            fill_color = "white"
        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        self._win.draw_line(line=left_wall, fill_color=fill_color)
        
        if self.has_bottom_wall:
            fill_color = "black"
        else:
            fill_color = "white"
        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        self._win.draw_line(line=bottom_wall, fill_color=fill_color)
        
        if self.has_right_wall:
            fill_color = "black"
        else:
            fill_color = "white"
        right_wall = Line(Point(self._x2, self._y2), Point(self._x2, self._y1))
        self._win.draw_line(line=right_wall, fill_color=fill_color)
        
        if self.has_top_wall:
            fill_color = "black"
        else:
            fill_color = "white"
        top_wall = Line(Point(self._x2, self._y1), Point(self._x1, self._y1))
        self._win.draw_line(line=top_wall, fill_color=fill_color)
      
        
    def draw_move(self, cell_dest, undo=False):
        def find_center(cell : Cell):               
            center_x = ((cell._x2 - cell._x1) / 2) + cell._x1
            center_y = ((cell._y2 - cell._y1) / 2) + cell._y1
            return center_x, center_y
        if undo:
            fill_color = "red"
        else:
            fill_color = "grey"
        
        path = Line(Point(find_center(self)[0], find_center(self)[1]), Point(find_center(cell_dest)[0], find_center(cell_dest)[1]))
        
        self._win.draw_line(line=path, fill_color=fill_color)
    
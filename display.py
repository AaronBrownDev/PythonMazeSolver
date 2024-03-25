from tkinter import Tk, BOTH, Canvas

class Window():
    
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
            
    def draw_line(self, line, fill_color : str):
        line.draw(self.__canvas, fill_color)
        
    def close(self):
        self.__running = False
        
        
class Point():
    
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
        

class Line():
    
    def __init__(self, p1 : Point, p2 : Point) -> None:
        self.point_one = p1
        self.point_two = p2
    
    def draw(self, canvas : Canvas, fill_color : str):
        canvas.create_line(
           self.point_one.x, self.point_one.y, self.point_two.x, self.point_two.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)
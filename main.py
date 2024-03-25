from display import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    
    cell_one = Cell(win)
    cell_one.draw(10, 10, 50, 50)
    
    win.wait_for_close()
    
main()

from display import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    window_size_x = 800
    window_size_y = 600
    num_cols = 14
    num_rows = 12
    spacing = 30
    cell_len_x = (window_size_x - spacing) / num_cols
    cell_len_y = (window_size_y - spacing) / num_rows
    
    win = Window(window_size_x, window_size_y)
    
    maze = Maze(spacing / 2, spacing / 2, num_cols, num_rows, cell_len_x, cell_len_y, win)
    
    # cell_one = Cell(win)
    # cell_two = Cell(win)
    
    # cell_one.draw(10, 10, 50, 50)
    # cell_two.draw(50, 10, 90, 50)
    
    # cell_one.draw_move(cell_two)
    
    win.wait_for_close()
    
main()

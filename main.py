from display import Window
from maze import Maze

def main():
    window_size_x = 1080
    window_size_y = 600
    num_cols = 10
    num_rows = 10
    spacing = 30
    cell_len_x = (window_size_x - spacing) / num_cols
    cell_len_y = (window_size_y - spacing) / num_rows
    
    win = Window(window_size_x, window_size_y)
    
    maze = Maze(spacing / 2, spacing / 2, num_cols, num_rows, cell_len_x, cell_len_y, win, 1)
    
    win.wait_for_close()
    
main()

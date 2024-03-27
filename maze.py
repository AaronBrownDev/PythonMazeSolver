from cell import Cell
import time, random

class Maze():
    
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed = None) -> None:
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        random.seed = seed
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    
    def _create_cells(self):
        for _ in range(self.num_rows):
            row = []
            for _ in range(self.num_cols):
                row.append(Cell(self._win))
            self._cells.append(row)
            
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

            
    def _draw_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
       
        
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
       
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self.num_rows-1, self.num_cols-1)
        
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            
            if i + 1 < self.num_rows and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))             
            if j + 1 < self.num_cols and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            chosen = random.choice(to_visit)
            
            if chosen[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            elif chosen[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False   
            elif chosen[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False   
            elif chosen[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False    
            
            self._break_walls_r(chosen[0], chosen[1])
            
    
    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False
                
    
    def solve(self):
        self._solve_r(i=0, j=0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True
    
        if i + 1 < self.num_rows and not self._cells[i+1][j].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                 self._cells[i][j].draw_move(self._cells[i+1][j], True)
        if i > 0 and not self._cells[i-1][j].visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                 self._cells[i][j].draw_move(self._cells[i-1][j], True)
        if j + 1 < self.num_cols and not self._cells[i][j+1].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
        if j > 0 and not self._cells[i][j-1].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                 self._cells[i][j].draw_move(self._cells[i][j-1], True)

        return False
        
        
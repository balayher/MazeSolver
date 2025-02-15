import time
import random
from cell import Cell

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
    
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j, sleep=0.01):
        if self._win is None:
            return
        x1 = self._x1 + (i * self._cell_size_x)
        x2 = self._x1 + ((i+1) * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        y2 = self._y1 + ((j+1) * self._cell_size_y)
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        if self._cells == []:
            return
        self._cells[0][0].top_wall = False
        self._draw_cell(0, 0)
        i = self._num_cols - 1
        j = self._num_rows - 1
        self._cells[i][j].bottom_wall = False
        self._draw_cell(i, j)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            list_ij = []

            # determining where to go next
            # left wall
            if i > 0:
                if self._cells[i-1][j].visited == False:
                    list_ij.append((i-1, j))
            # right wall
            if i < self._num_cols - 1:
                if self._cells[i+1][j].visited == False:
                    list_ij.append((i+1, j))
            # top wall
            if j > 0:
                if self._cells[i][j-1].visited == False:
                    list_ij.append((i, j-1))
            # bottom wall
            if j < self._num_rows - 1:
                if self._cells[i][j+1].visited == False:
                    list_ij.append((i, j+1))

            # if no walls exit
            if len(list_ij) == 0:
                self._draw_cell(i, j)
                return

            # choose random direction
            direction = random.randrange(len(list_ij))
            x = list_ij[direction][0]
            y = list_ij[direction][1]

            #breaking walls
            # left wall
            if x < i:
                self._cells[i][j].left_wall = False
                self._draw_cell(i, j)
                self._cells[x][j].right_wall = False
                self._draw_cell(x, j)
            # right wall
            if x > i:
                self._cells[i][j].right_wall = False
                self._draw_cell(i, j)
                self._cells[x][j].left_wall = False
                self._draw_cell(x, j)
            # top wall
            if y < j:
                self._cells[i][j].top_wall = False
                self._draw_cell(i, j)
                self._cells[i][y].bottom_wall = False
                self._draw_cell(i, y)
            # bottom wall
            if y > j:
                self._cells[i][j].bottom_wall = False
                self._draw_cell(i, j)
                self._cells[i][y].top_wall = False
                self._draw_cell(x, j)

            # to next cell
            self._break_walls_r(x, y)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()

        # visiting current cell
        self._cells[i][j].visited = True

        # if this is end cell, we are done
        if i == (self._num_cols -1) and j == (self._num_rows -1):
            return True

        # to move left
        if self._cells[i][j].left_wall == False:
            if self._cells[i-1][j].visited == False and self._cells[i-1][j].right_wall == False:
                self._cells[i][j].draw_move(self._cells[i-1][j])
                time.sleep(0.05)
                if self._solve_r(i-1, j) == True:
                    return True
                time.sleep(0.05)
                self._cells[i-1][j].draw_move(self._cells[i][j], True)
                time.sleep(0.05)
        # to move right
        if self._cells[i][j].right_wall == False:
            if self._cells[i+1][j].visited == False and self._cells[i+1][j].left_wall == False:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                time.sleep(0.05)
                if self._solve_r(i+1, j) == True:
                    return True
                time.sleep(0.05)
                self._cells[i+1][j].draw_move(self._cells[i][j], True)
                time.sleep(0.05)
        # to move up
        if self._cells[i][j].top_wall == False:
            if self._cells[i][j-1].visited == False and self._cells[i][j-1].bottom_wall == False:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                time.sleep(0.05)
                if self._solve_r(i, j-1) == True:
                    return True
                time.sleep(0.05)
                self._cells[i][j-1].draw_move(self._cells[i][j], True)
                time.sleep(0.05)
        # to move down
        if self._cells[i][j].bottom_wall == False:
            if self._cells[i][j+1].visited == False and self._cells[i][j+1].top_wall == False:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                time.sleep(0.05)
                if self._solve_r(i, j+1) == True:
                    return True
                time.sleep(0.05)
                self._cells[i][j+1].draw_move(self._cells[i][j], True)
                time.sleep(0.05)
        
        return False
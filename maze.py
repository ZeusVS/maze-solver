from cell import Cell
import random
import time

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                col_cells.append(cell)
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        if self._win == None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_dir = []
            if i >= 1:
                if self._cells[i - 1][j].visited == False:
                    possible_dir.append([i - 1, j])
            if i <= self._num_cols - 2:
                if self._cells[i + 1][j].visited == False:
                    possible_dir.append([i + 1, j])
            if j >= 1:
                if self._cells[i][j - 1].visited == False:
                    possible_dir.append([i, j - 1])
            if j <= self._num_rows - 2:
                if self._cells[i][j + 1].visited == False:
                    possible_dir.append([i, j + 1])

            if possible_dir == []:
                self._draw_cell(i, j)
                return

            dest = random.choice(possible_dir) 

            if dest[0] > i:
                self._cells[i][j].has_right_wall = False
                self._cells[dest[0]][j].has_left_wall = False
            elif dest[0] < i:
                self._cells[i][j].has_left_wall = False
                self._cells[dest[0]][j].has_right_wall = False
            elif dest[1] > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][dest[1]].has_top_wall = False
            elif dest[1] < j:
                self._cells[i][j].has_top_wall = False
                self._cells[i][dest[1]].has_bottom_wall = False

            self._break_walls_r(dest[0], dest[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _solve_r(self, i, j):
        self._animate()

        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        possible_dir = []

        if (i >= 1 
            and not self._cells[i][j].has_left_wall
            and self._cells[i - 1][j].visited == False
        ):
            possible_dir.append([i - 1, j])

        if (i <= self._num_cols - 2 
            and not self._cells[i][j].has_right_wall
            and self._cells[i + 1][j].visited == False
        ):
            possible_dir.append([i + 1, j])

        if (j >= 1 
            and not self._cells[i][j].has_top_wall
            and self._cells[i][j - 1].visited == False
        ):
            possible_dir.append([i, j - 1])

        if (j <= self._num_rows - 2 
            and not self._cells[i][j].has_bottom_wall
            and self._cells[i][j + 1].visited == False
        ):
            possible_dir.append([i, j + 1])

        while possible_dir:
            dest = possible_dir.pop()
            self._cells[i][j].draw_move(self._cells[dest[0]][dest[1]])
            correct = self._solve_r(dest[0], dest[1])
            if correct:
                return True
            self._cells[i][j].draw_move(self._cells[dest[0]][dest[1]], True)

        return False
    
    def solve(self):
        return self._solve_r(0, 0)

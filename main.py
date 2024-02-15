from graphics import Window
from cell import Cell
from maze import Maze


def main():
    num_cols = 16
    num_rows = 12
    margin = 50
    screen_x = 900
    screen_y = 700
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    # Remove seed argument for random maze generation
    # seed = 0

    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, 
                cell_size_x, cell_size_y, win)
    maze.solve()
    win.wait_for_close()


main()

from window import Window
from grid import Cell, Grid
from buttons import Buttons

def main():
    window = Window(600, 800)
    grid = Grid([10, 10], 100, window)
    buttons = Buttons(window, [400, 10], 100, grid.grid)
    grid.update()
    window.wait_for_close()

main()

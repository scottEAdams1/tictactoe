from window import Window
from grid import Cell, Grid

def main():
    window = Window(600, 800)
    grid = Grid([10, 10], 100, window)
    window.wait_for_close()

main()

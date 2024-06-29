from window import Window
from grid import Cell, Grid
from buttons import Buttons
from open_screen import OpenScreen

def main():
    window = Window(600, 800)
    start = OpenScreen(window)
    
    window.wait_for_close()

main()

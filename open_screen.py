import tkinter as tk
from tkinter import ttk
from grid import Cell, Grid
from buttons import Buttons

class OpenScreen:
    def __init__(self, window):
        self.window = window
        self.canvas = window.get_canvas()
        self.root = window.get_root()
        self.start()

    ##Starts the game
    def start_game(self, event):
        self.canvas.delete("start")
        event.place_forget()
        grid = Grid([10, 10], 100, self.window)
        buttons = Buttons(self.window, [10, 10], 100, grid)
        grid.update(buttons.buttons)
        
    ##Sets up the starting screen
    def start(self):
        self.canvas.create_text(300, 25, font = ("Arial", 35),
        fill = "red", text = "TicTacToe", tags = ("start",))
        self.button = tk.Button(self.root, text = "Start",
        command = lambda: self.start_game(self.button))
        self.button.pack()
        self.button.place(x = 300, y = 400)

    
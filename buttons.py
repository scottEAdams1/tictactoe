import tkinter as tk
from tkinter import ttk
from grid import Grid
 

class Button:
    def __init__(self, window, size, point, cell):
        self.point = point
        self.root = window.get_root()
        self.size = size
        self.cell = cell
        self.create_button()
        
    ##If a button is clicked, set that cell to an X,
    ##and remove the button there
    def button_clicked(self, event):
        if self.cell.type == "":
            self.cell.type = "X"
            event.place_forget()
            
    ##Create a button for the cell
    def create_button(self):
        self.button = tk.Button(self.root, text = "",
        command = lambda: self.button_clicked(self.button))
        self.button.pack()
        self.button.place(x = self.point[0],y = self.point[1],
        width = self.size, height = self.size)


class Buttons:
    def __init__(self, window, point, size, grid):
        self.point = point
        self.size = size
        self.window = window
        self.root = window.get_root()
        self.buttons = []
        self.grid = grid
        self.cells = grid.grid
        self.create_buttons()
        self.reset_button()

    ##Create buttons for each of the cells in the grid
    def create_buttons(self):
        for i in range(3):
            col = []
            for j in range(3):
                col.append(Button(self.window, self.size,
                [self.point[0] + self.size * i, self.point[1] + self.size * j],
                self.cells[i][j]))
            self.buttons.append(col)
    
    ##Create a reset button to reset the game
    def reset_button(self):
        button = tk.Button(self.root, text = "Reset",
        command = self.reset)
        button.place(x = 400, y = 10)

    ##Reset each of the cells, buttons, and the win text
    def reset(self):
        ##Reset the cells value, and replace the buttons
        for i in range(3):
            for j in range(3):
                self.cells[i][j].type = ""
                self.buttons[i][j].button.place(x = self.point[0] + self.size * i,
                y = self.point[1] + self.size * j,
                width = self.size, height = self.size)
        ##Reset the text and the shapes in the cells
        self.window.get_canvas().delete("move")
        ##Rerun the update function
        self.grid.update(self.buttons)

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
        
    
    def button_clicked(self, event):
        if self.cell.type == "":
            self.cell.type = "X"
            event.place_forget()
            

    def create_button(self):
        self.button = tk.Button(self.root, text = "", command = lambda: self.button_clicked(self.button))
        self.button.pack()
        self.button.place(x = self.point[0],y = self.point[1], width = self.size, height = self.size)


class Buttons:
    def __init__(self, window, point, size, cells):
        self.point = point
        self.size = size
        self.window = window
        self.root = window.get_root()
        self.buttons = []
        self.cells = cells
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            col = []
            for j in range(3):
                col.append(Button(self.window, self.size,
                [self.point[0] + self.size * i, self.point[1] + self.size * j],
                self.cells[i][j]))
            self.buttons.append(col)

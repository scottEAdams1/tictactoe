from tkinter import *
from tkinter import messagebox

##Determines if a win condition has been met
def win(cells, window):
    canvas = window.get_canvas()
    ##Checks if there are three of the same type in a column
    if (cells[0][0].type == cells[0][1].type
    and cells[0][1].type == cells[0][2].type
    and cells[0][0].type != ""):
        canvas.create_text(300, 400, font = ("Arial", 30), fill = "red",
        text = f"Winner is {cells[0][0].type}!!!", tags=("move",))
        return True
    if (cells[1][0].type == cells[1][1].type
    and cells[1][1].type == cells[1][2].type
    and cells[1][0].type != ""):
        canvas.create_text(300, 400, font = ("Arial", 30), fill = "red",
        text = f"Winner is {cells[1][0].type}!!!", tags=("move",))
        return True
    if (cells[2][0].type == cells[2][1].type
    and cells[2][1].type == cells[2][2].type
    and cells[2][0].type != ""):
        canvas.create_text(300, 400, font = ("Arial", 30), fill = "red",
        text = f"Winner is {cells[2][0].type}!!!", tags=("move",))
        return True

    ##Checks if there are three of the same type in a row
    if (cells[0][0].type == cells[1][0].type
    and cells[1][0].type == cells[2][0].type
    and cells[0][0].type != ""):
        canvas.create_text(300, 400, font = ("Arial", 30), fill = "red",
        text = f"Winner is {cells[0][0].type}!!!", tags=("move",))
        return True
    if (cells[0][1].type == cells[1][1].type
    and cells[1][1].type == cells[2][1].type
    and cells[0][1].type != ""):
        canvas.create_text(300, 400, font = ("Arial", 30), fill = "red",
        text = f"Winner is {cells[0][1].type}!!!", tags=("move",))
        return True
    if (cells[0][2].type == cells[1][2].type
    and cells[1][2].type == cells[2][2].type
    and cells[0][2].type != ""):
        canvas.create_text(300, 400, font = ("Arial", 30), fill = "red",
        text = f"Winner is {cells[0][2].type}!!!", tags=("move",))
        return True

    ##Checks if there are three of the same type in a diagonal
    if (cells[0][0].type == cells[1][1].type
    and cells[1][1].type == cells[2][2].type
    and cells[0][0].type != ""):
        canvas.create_text(300, 400, font = ("Arial", 30), fill = "red",
        text = f"Winner is {cells[0][0].type}!!!", tags=("move",))
        return True
    if (cells[0][2].type == cells[1][1].type
    and cells[1][1].type == cells[2][0].type
    and cells[0][2].type != ""):
        canvas.create_text(300, 400, font = ("Arial", 30), fill = "red",
        text = f"Winner is {cells[0][2].type}!!!", tags=("move",))
        return True
    return False
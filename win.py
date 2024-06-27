from tkinter import *
from tkinter import messagebox

def win(cells, window):
    canvas = window.get_canvas()
    if (cells[0][0].type == cells[0][1].type
    and cells[0][1].type == cells[0][2].type
    and cells[0][0].type != ""):
        canvas.create_text(300, 400, text = f"Winner is {cells[0][0].type}")
        return True
    if (cells[1][0].type == cells[1][1].type
    and cells[1][1].type == cells[1][2].type
    and cells[1][0].type != ""):
        canvas.create_text(300, 400, text = f"Winner is {cells[1][0].type}")
        return True
    if (cells[2][0].type == cells[2][1].type
    and cells[2][1].type == cells[2][2].type
    and cells[2][0].type != ""):
        canvas.create_text(300, 400, text = f"Winner is {cells[2][0].type}")
        return True
    if (cells[0][0].type == cells[1][0].type
    and cells[1][0].type == cells[2][0].type
    and cells[0][0].type != ""):
        canvas.create_text(300, 400, text = f"Winner is {cells[0][0].type}")
        return True
    if (cells[0][1].type == cells[1][1].type
    and cells[1][1].type == cells[2][1].type
    and cells[0][1].type != ""):
        canvas.create_text(300, 400, text = f"Winner is {cells[0][1].type}")
        return True
    if (cells[0][2].type == cells[1][2].type
    and cells[1][2].type == cells[2][2].type
    and cells[0][2].type != ""):
        canvas.create_text(300, 400, text = f"Winner is {cells[0][2].type}")
        return True
    if (cells[0][0].type == cells[1][1].type
    and cells[1][1].type == cells[2][2].type
    and cells[0][0].type != ""):
        canvas.create_text(300, 400, text = f"Winner is {cells[0][0].type}")
        return True
    if (cells[0][2].type == cells[1][1].type
    and cells[1][1].type == cells[2][0].type
    and cells[0][2].type != ""):
        canvas.create_text(300, 400, text = f"Winner is {cells[0][2].type}")
        return True
    return False
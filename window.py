from tkinter import Tk, Canvas, BOTH

class Window:
    def __init__(self, height, width):
        self.__root = Tk()
        self.__root.title = "Tic Tac Toe"
        self.__canvas = Canvas(self.__root, bg = "light blue", height = height, width = width)
        self.__canvas.pack(fill = BOTH, expand = 1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()

    def close(self):
        self.__running = False
import time, random
from win import win

class Cell:
    def __init__(self, point, size, canvas):
        self.x = point[0]
        self.y = point[1]
        self.size = size
        self.canvas = canvas
        self.type = ""

    ##Create a single line
    def create_line(self, point1, point2, tags=None):
        self.canvas.create_line(point1[0], point1[1], point2[0], point2[1],
        fill = "black", width = 2, tags = tags)

    ##Create a box for the grid
    def create_box(self):
        ##Top
        self.create_line([self.x, self.y], [self.x + self.size, self.y])
        ##Left
        self.create_line([self.x, self.y], [self.x, self.y + self.size])
        ##Bottom
        self.create_line([self.x, self.y + self.size],
        [self.x + self.size, self.y + self.size])
        ##Right
        self.create_line([self.x + self.size, self.y],
        [self.x + self.size, self.y + self.size])

    ##Add an X to the box, player 1
    def add_x(self):
        self.create_line([self.x, self.y],
        [self.x + self.size, self.y + self.size], tags = ("move",))
        self.create_line([self.x, self.y + self.size],
        [self.x + self.size, self.y], tags = ("move",))

    ##Add an O to the box, player 2 (computer)
    def add_o(self):
        self.canvas.create_oval(self.x, self.y, self.x + self.size,
        self.y + self.size, width = 2, tags = ("move",))
    
class Grid:
    def __init__(self, point, size, window):
        self.x = point[0]
        self.y = point[1]
        self.size = size
        self.grid = []
        self.window = window
        self.populate_grid()
        
    ##Create 9 cells in a 3x3 grid
    def populate_grid(self):
        for i in range(3):
            col = []
            for j in range(3):
                col.append(Cell([self.x + self.size * i, self.y + self.size * j],
                self.size, self.window.get_canvas()))
            self.grid.append(col)
        self.draw_grid()

    ##Draw the grid out with the correct moves if there are any
    def draw_grid(self):
        for i in range(3):
            for j in range(3):
                self.grid[i][j].create_box()
                if self.grid[i][j].type == "X":
                    self.grid[i][j].add_x()
                elif self.grid[i][j].type == "O":
                    self.grid[i][j].add_o()
        self._animate()

    ##Update the display window
    def _animate(self):
        if self.window != None:
            self.window.redraw()
            time.sleep(0.05)
    
    ##Update the window after each move,
    ##checking if there has been a win yet
    def update(self, buttons):
        finished = False
        
        ##Continuous loop
        while finished == False:
            ##Computer (O) makes a move
            self.player2(buttons)
            self.draw_grid()
            ##Check for win condition to be met
            finished = win(self.grid, self.window)
            ##Check for a tie
            if self.count() == 8 and finished == False:
                self.window.get_canvas().create_text(300, 400,
                font = ("Arial", 30), fill = "red", text = "Tie",
                tags = ("move",))
                finished = True
            
        self.draw_grid()

    ##Player 2 (computer) makes a move depending on the current state
    ##of the grid
    def player2(self, buttons):
        ##Computer has 2 squares in a column, can place a third and win
        if self.count() % 2 != 0:
            for i in range(3):
                if (self.grid[i][0].type == self.grid[i][1].type
                and self.grid[i][0].type == "O"
                and self.grid[i][2].type == ""):
                    self.grid[i][2].type = "O"
                    buttons[i][2].button.place_forget()
                    break
                elif (self.grid[i][0].type == self.grid[i][2].type
                and self.grid[i][0].type == "O"
                and self.grid[i][1].type == ""):
                    self.grid[i][1].type = "O"
                    buttons[i][1].button.place_forget()
                    break
                elif (self.grid[i][2].type == self.grid[i][1].type
                and self.grid[i][0].type == "O"
                and self.grid[i][0].type == ""):
                    self.grid[i][0].type = "O"
                    buttons[i][0].button.place_forget()
                    break

        ##Computer has 2 squares in a row, can place a third and win
        if self.count() % 2 != 0:
            for i in range(3):
                if (self.grid[0][i].type == self.grid[1][i].type
                and self.grid[0][i].type == "O" and
                self.grid[2][i].type == ""):
                    self.grid[2][i].type = "O"
                    buttons[2][i].button.place_forget()
                    break
                elif (self.grid[0][i].type == self.grid[2][i].type
                and self.grid[0][i].type == "O"
                and self.grid[1][i].type == ""):
                    self.grid[1][i].type = "O"
                    buttons[1][i].button.place_forget()
                    break
                elif (self.grid[2][i].type == self.grid[1][i].type
                and self.grid[0][i].type == "O"
                and self.grid[0][i].type == ""):
                    self.grid[0][i].type = "O"
                    buttons[0][i].button.place_forget()
                    break

        ##Computer has 2 squares in a diagonal, can place a third and win
        if self.count() % 2 != 0:
            if (self.grid[0][0].type == self.grid[2][2].type
            and self.grid[0][0].type == "O"
            and self.grid[1][1].type == ""):
                self.grid[1][1].type = "O"
                buttons[1][1].button.place_forget()
            elif (self.grid[0][0].type == self.grid[1][1].type
            and self.grid[0][0].type == "O"
            and self.grid[2][2].type == ""):
                self.grid[2][2].type = "O"
                buttons[2][2].button.place_forget()
            elif (self.grid[2][2].type == self.grid[1][1].type
            and self.grid[2][2].type == "O"
            and self.grid[0][0].type == ""):
                self.grid[0][0].type = "O"
                buttons[0][0].button.place_forget()
            elif (self.grid[0][2].type == self.grid[1][1].type
            and self.grid[0][2].type == "O"
            and self.grid[2][0].type == ""):
                self.grid[2][0].type = "O"
                buttons[2][0].button.place_forget()
            elif (self.grid[0][2].type == self.grid[2][0].type
            and self.grid[0][2].type == "O"
            and self.grid[1][1].type == ""):
                self.grid[1][1].type = "O"
                buttons[1][1].button.place_forget()
            elif (self.grid[2][0].type == self.grid[1][1].type
            and self.grid[2][0].type == "O"
            and self.grid[0][2].type == ""):
                self.grid[0][2].type = "O"
                buttons[0][2].button.place_forget()

        ##Player has 2 moves in a column,
        ##computer can stop them from winning
        if self.count() % 2 != 0:
            for i in range(3):
                if (self.grid[i][0].type == self.grid[i][1].type
                and self.grid[i][0].type == "X"
                and self.grid[i][2].type == ""):
                    self.grid[i][2].type = "O"
                    buttons[i][2].button.place_forget()
                    break
                elif (self.grid[i][0].type == self.grid[i][2].type
                and self.grid[i][0].type == "X"
                and self.grid[i][1].type == ""):
                    self.grid[i][1].type = "O"
                    buttons[i][1].button.place_forget()
                    break
                elif (self.grid[i][2].type == self.grid[i][1].type
                and self.grid[i][0].type == "X"
                and self.grid[i][0].type == ""):
                    self.grid[i][0].type = "O"
                    buttons[i][0].button.place_forget()
                    break
        
        ##Player has 2 moves in a row,
        ##computer can stop them from winning
        if self.count() % 2 != 0:
            for i in range(3):
                if (self.grid[0][i].type == self.grid[1][i].type
                and self.grid[0][i].type == "X"
                and self.grid[2][i].type == ""):
                    self.grid[2][i].type = "O"
                    buttons[2][i].button.place_forget()
                    break
                elif (self.grid[0][i].type == self.grid[2][i].type
                and self.grid[0][i].type == "X"
                and self.grid[1][i].type == ""):
                    self.grid[1][i].type = "O"
                    buttons[1][i].button.place_forget()
                    break
                elif (self.grid[2][i].type == self.grid[1][i].type
                and self.grid[0][i].type == "X"
                and self.grid[0][i].type == ""):
                    self.grid[0][i].type = "O"
                    buttons[0][i].button.place_forget()
                    break

        ##Player has 2 moves in a diagonal,
        ##computer can stop them from winning
        if self.count() % 2 != 0:
            if (self.grid[0][0].type == self.grid[2][2].type
            and self.grid[0][0].type == "X"
            and self.grid[1][1].type == ""):
                self.grid[1][1].type = "O"
                buttons[1][1].button.place_forget()
            elif (self.grid[0][0].type == self.grid[1][1].type
            and self.grid[0][0].type == "X"
            and self.grid[2][2].type == ""):
                self.grid[2][2].type = "O"
                buttons[2][2].button.place_forget()
            elif (self.grid[2][2].type == self.grid[1][1].type
            and self.grid[2][2].type == "X"
            and self.grid[0][0].type == ""):
                self.grid[0][0].type = "O"
                buttons[0][0].button.place_forget()
            elif (self.grid[0][2].type == self.grid[1][1].type
            and self.grid[0][2].type == "X"
            and self.grid[2][0].type == ""):
                self.grid[2][0].type = "O"
                buttons[2][0].button.place_forget()
            elif (self.grid[0][2].type == self.grid[2][0].type
            and self.grid[0][2].type == "X"
            and self.grid[1][1].type == ""):
                self.grid[1][1].type = "O"
                buttons[1][1].button.place_forget()
            elif (self.grid[2][0].type == self.grid[1][1].type
            and self.grid[2][0].type == "X"
            and self.grid[0][2].type == ""):
                self.grid[0][2].type = "O"
                buttons[0][2].button.place_forget()

        ##There are no ways of winning the game in a move,
        ##place an O at random
        if self.count() % 2 != 0:
            while self.count() % 2 != 0:
                i = random.randint(0, 2)
                j = random.randint(0, 2)
                if self.grid[i][j].type == "":
                    self.grid[i][j].type = "O"
                    buttons[i][j].button.place_forget()

    ##Counts the number of taken cells
    def count(self):
        total = 0
        for i in range(3):
            for j in range(3):
                if self.grid[i][j].type != "":
                    total += 1
        return total

    

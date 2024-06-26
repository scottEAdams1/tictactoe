import time

class Cell:
    def __init__(self, point, size, canvas):
        self.x = point[0]
        self.y = point[1]
        self.size = size
        self.canvas = canvas

    def create_line(self, point1, point2):
        self.canvas.create_line(point1[0], point1[1], point2[0], point2[1], fill = "black", width = 2)

    def create_box(self):
        ##Top
        self.create_line([self.x, self.y], [self.x + self.size, self.y])
        ##Left
        self.create_line([self.x, self.y], [self.x, self.y + self.size])
        ##Bottom
        self.create_line([self.x, self.y + self.size], [self.x + self.size, self.y + self.size])
        ##Right
        self.create_line([self.x + self.size, self.y], [self.x + self.size, self.y + self.size])

    
class Grid:
    def __init__(self, point, size, window):
        self.x = point[0]
        self.y = point[1]
        self.size = size
        self.grid = []
        self.window = window
        self.populate_grid()
        

    def populate_grid(self):
        for i in range(3):
            col = []
            for j in range(3):
                col.append(Cell([self.x + self.size * i, self.y + self.size * j], self.size, self.window.get_canvas()))
            self.grid.append(col)
        self.draw_grid()

    def draw_grid(self):
        for i in range(3):
            for j in range(3):
                self.grid[i][j].create_box()
        self._animate()

    def _animate(self):
        if self.window != None:
            self.window.redraw()
            time.sleep(0.05)
    

    

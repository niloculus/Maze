import turtle
SIZE = 400
EAST=0
NORTH=1
WEST=2
SOUTH=3
class Maze:
    def __init__(self):
        self.reset()
    def get_turtle(self):
        self.t = turtle.turtles()[0]
        return (self.t)
    def reset(self):
        self.screen = turtle.getscreen()
        turtle.setup(400, 400)
        self.t = turtle.turtles()[0]
        self.t.penup()
        self.t.goto(-(SIZE / 2 - 20), SIZE / 2 - 20)
        self.matrix = [[1 for i in range(int(SIZE / 20))] for i in range(int(SIZE / 20))]
        self.screen.bgcolor('blue')
        self.t.shape('square')
        self.t.color('white')
        self.t.stamp()
        self.matrix[0][0] = 0
    def getMatrixValueAt(self, pos):
        m = Maze()
        m.reset()
        x = int((pos[0] + 180) / 20)
        y = 20 - int((pos[1] + 200) / 20) - 1
        v = self.matrix[x][y]
        return v
    def setMatrixValueAt(self, pos, value):
        x = int((pos[0] + 200) / 20)
        y = 20 - int((pos[1] + 200) / 20) - 1
        try:
            self.matrix[y][x] = value
        except:
            return False
        if value == 0:
            self.t.color('white')
            self.t.stamp()
        if value == 1:
            self.t.color('blue')
            self.t.stamp()
            return True



# def dig(self, d):
    #     return self.t.pos()



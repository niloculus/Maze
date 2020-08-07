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
        turtle.setup(400*1.3, 400*1.3)
        self.t = turtle.turtles()[0]
        self.t.penup()
        self.t.goto(-(SIZE / 2 - 20), SIZE / 2 - 20)
        self.matrix = [[1 for i in range(int(SIZE / 20))] for i in range(int(SIZE / 20))]
        self.screen.bgcolor('blue')
        self.t.shape('square')
        self.t.color('white')
        self.t.stamp()
        self.matrix[0][0] = 0
    def fourcorners(self):
        self.t.goto(-180, 180)
        self.t.stamp()
        self.t.goto(-180, -200)
        self.t.stamp()
        self.t.goto(200, -200)
        self.t.stamp()
        self.t.goto(200, 180)
        self.t.stamp()
    def dig(self, d):
        p = self.t.pos()
        if d == EAST:
            if p[0] == 180:
                return p
            else:
                newpos = (p[0] + 20, p[1])
                self.t.stamp()
                self.t.goto(newpos)
                i,j = self.pos2index(newpos)
                self.matrix[i][j] = 0
        if d == WEST:
            if p[0] == -180:
                return p
            else:
                newpos = (p[0] - 20, p[1])
                self.t.goto(newpos)
                i, j = self.pos2index(newpos)
                self.matrix[i][j] = 0
        if d == NORTH:
            if p[1] == 180:
                return p
            else:
                newpos = (p[0], p[1] + 20)
                self.t.goto(newpos)
                i, j = self.pos2index(newpos)
                self.matrix[i][j] = 0
        if d == SOUTH:
            if p[1] == -200:
                return p
            else:
                newpos = (p[0], p[1] - 20)
                self.t.goto(newpos)
                i, j = self.pos2index(newpos)
                self.matrix[i][j] = 0
    def pos2index(self, p):
        """ converts tuple p into tuple idx
        200,-200 == 19,19
        -180,180 == 0,0
        -180,-200 == 0,19
        200,180 == 19,0 """

        i = int((p[0] + 180) / 20)
        j = int((180 - p[1]) / 20)
        return ((i, j))

    def getMatrixValueAt(self, pos):
        x = int((pos[0] + 180) / 20)
        y = int((pos[1] - 180) / 20)
        v = self.matrix[x][y]
        return v
    def setMatrixValueAt(self, pos, value):
        x = int((pos[0] + 180) / 20)
        y = int((pos[1] - 180) / 20)
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







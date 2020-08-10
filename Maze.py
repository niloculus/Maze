import turtle
import random

SIZE = 400

EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Maze:
    """ This class creates a random maze """

    def __init__(self):
        self.matrix = [[1 for i in range(int(SIZE / 20))] for i in range(int(SIZE / 20))]
        self.turtle = turtle.Turtle()
        self.s = turtle.Screen()
        self.reset()

    def reset(self):
        self.s.bgcolor('blue')
        self.turtle.penup()
        self.s.setup(width=SIZE * 1.3, height=SIZE * 1.3)
        self.turtle.goto(-(SIZE / 2 - 20), SIZE / 2 - 20)
        self.turtle.shape('square')
        self.turtle.color('white')
        self.turtle.stamp()
        self.matrix[0][0] = 0
        self.depth = 0
        self.goal = (-180,180)

    def fourcorners(self):
        self.turtle.goto(-180, 180)
        self.turtle.stamp()
        self.turtle.goto(-180, -200)
        self.turtle.stamp()
        self.turtle.goto(200, -200)
        self.turtle.stamp()
        self.turtle.goto(200, 180)
        self.turtle.stamp()

    def dig(self, d):
        p = self.turtle.pos()
        # (-180,180) for instance
        if d == EAST:
            newpos = (p[0] + 20, p[1])
            i0, j0 = self.pos2index(p)
            matrix_value = self.matrix[i0 + 2][j0]
            if matrix_value == 0:
                return p
            self.turtle.goto(newpos)
            self.turtle.stamp()
            i, j = self.pos2index(newpos)
            self.matrix[i][j] = 0
        if d == WEST:
            if p[0] == -180:
                return p
            else:
                newpos = (p[0] - 20, p[1])
                i0, j0 = self.pos2index(p)
                matrix_value = self.matrix[i0 - 2][j0]
                if matrix_value == 0:
                    return p
                self.turtle.goto(newpos)
                self.turtle.stamp()
                i, j = self.pos2index(newpos)
                self.matrix[i][j] = 0
        if d == NORTH:
            if p[1] == 180:
                return p
            else:
                newpos = (p[0], p[1] + 20)
                i0, j0 = self.pos2index(p)
                matrix_value = self.matrix[i0][j0 - 2]
                if matrix_value == 0:
                    return p
                self.turtle.goto(newpos)
                self.turtle.stamp()
                i, j = self.pos2index(newpos)
                self.matrix[i][j] = 0
        if d == SOUTH:
            if p[1] == -200:
                return p
            else:
                newpos = (p[0], p[1] - 20)
                i0, j0 = self.pos2index(p)
                matrix_value = self.matrix[i0][j0 + 2]
                if matrix_value == 0:
                    return p
                self.turtle.goto(newpos)
                self.turtle.stamp()
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
        return i, j

    def getMatrixValueAt(self, pos):
        x = int((pos[0] + 180) / 20)
        y = int((180 - pos[1]) / 20)
        if x < 0 or x > 19 or y < 0 or y > 19:
            return -1
        v = self.matrix[x][y]
        return v

        # take (-180,180) and convert to [0][0] v = self.matrix[0][0]
        """ returns value of matrix at position pos """
        pass

    def setMatrixValueAt(self, pos, value):
        x = int((pos[0] + 180) / 20)
        y = int((pos[1] - 180) / 20)
        try:
            self.matrix[y][x] = value
        except():
            return False
        if value == 0:
            self.turtle.color('white')
            self.turtle.stamp()
        if value == 1:
            self.turtle.color('blue')
            self.turtle.stamp()
        return True

    def neighbors(self):
        p = self.turtle.position()
        r = []
        r.append((self.getMatrixValueAt((p[0] + 40, p[1])), EAST))
        r.append((self.getMatrixValueAt((p[0], p[1] + 40)), NORTH))
        r.append((self.getMatrixValueAt((p[0] - 40, p[1])), WEST))
        r.append((self.getMatrixValueAt((p[0], p[1] - 40)), SOUTH))
        return r

    def makeMaze(self):
        n = self.neighbors()
        oldpos = self.turtle.position()
        while len(n) > 0:
            nchoice = random.choice(n)
            n.remove(nchoice)
            self.turtle.goto(oldpos)
            if nchoice[0] == 1:
                d = nchoice[1]
                self.dig(d)
                self.dig(d)
                if self.turtle.pos()[0] > self.depth:
                    self.goal = self.turtle.pos()
                    self.depth = self.goal[1]
                self.depth = self.depth + 1
                self.makeMaze()
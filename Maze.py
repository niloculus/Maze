import turtle
SIZE = 400
class Maze:
    def __init__(self):
        self.screen = turtle.getscreen()
        turtle.setup(400, 400)
        self.matrix = [[1 for i in range(20)] for j in range(20)]
        # self.screen.screensize(400,400) works for 2nd and 3rd test_Size
    def get_turtle(self):
        self.t = turtle.turtles()[0]
        return (self.t)


    def reset(self):
        self.screen = turtle.getscreen()
        turtle.setup(400, 400)
        self.t = turtle.turtles()[0]
        self.t.penup()
        self.t.goto(-(SIZE / 2 - 10), SIZE / 2 - 10)
        self.matrix = [[1 for i in range(int(SIZE / 20))] for i in range(int(SIZE / 20))]
        self.b = turtle.bgcolor('blue')
        self.t.shape('square')
        self.t.color('white')
        self.t.stamp()
        self.matrix[0][0] = 0

    # def getMatrixValueAt(self, pos):
    #     m.reset()
    #     value = m.getMatrixValueAt(m.turtle.position)
    #     m.setMatrixValueAt(m.turtle.position, value)
    #     x = int((pos[0] + 200) / 20)
    #     y = 20 - int((pos[1] + 200) / 20) - 1
    #     # WRITE CODE TO ASSIGN THE MATRIX VALUE AT x,y TO v
    #     return v




        # self.screen.screensize(400, 400)
        # self.s = turtle.screensize(400, 400)


        # self.s.screensize(400, 400)







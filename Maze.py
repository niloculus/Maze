import turtle

class Maze:
    def __init__(self):
        self.screen = turtle.getscreen()
        turtle.setup(400, 400)
        self.matrix = [[1 for i in range(20)] for j in range(20)]
        # self.screen.screensize(400,400) works for 2nd and 3rd test_Size
    def get_turtle(self):
        self.t = turtle.turtles()[0]
        return (self.t)
    def bgcolor(self):
        self.b = turtle.bgcolor('blue')



        # self.screen.screensize(400, 400)
        # self.s = turtle.screensize(400, 400)


        # self.s.screensize(400, 400)







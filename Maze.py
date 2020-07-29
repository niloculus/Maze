import turtle
SIZE = 400
class Maze:
    def __init__(self):
        self.screen = turtle.getscreen()

    def get_turtle(self):
        self.t = turtle.turtles()[0]
        return (self.t)
    def bgcolor(self):
        self.b = turtle.bgcolor('blue')
    def screensize(self):
        self.s = turtle.getscreen()
        self.screen.setup(400, 400)
        # self.screen.screensize(400,400)

        # self.screen.screensize(400, 400)
        # self.s = turtle.screensize(400, 400)


        # self.s.screensize(400, 400)







import turtle

class Maze:
    def __init__(self):
        self.screen = turtle.getscreen()
        turtle.setup(400, 400)
        # self.screen.screensize(400,400)
    def get_turtle(self):
        self.t = turtle.turtles()[0]
        return (self.t)
    def bgcolor(self):
        self.b = turtle.bgcolor('blue')



        # self.screen.screensize(400, 400)
        # self.s = turtle.screensize(400, 400)


        # self.s.screensize(400, 400)







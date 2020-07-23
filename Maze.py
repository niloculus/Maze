import turtle


class Maze:
    def __init__(self):
        self.screen = turtle.getscreen()
    def get_turtle(self):
        self.t=turtle.turtles()[0]
        return(self.t)
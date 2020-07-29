import turtle
import unittest
SIZE = 400
from Maze import Maze

class MazeTests(unittest.TestCase):
    def setUp(self):
        self.m = Maze()
    def test_maze(self):
        self.assertTrue(type(self.m.screen) == turtle._Screen,"No Screen! type is" + str(type(self.m.screen)))
    def test_turtle(self):
        t = self.m.get_turtle()
        self.assertTrue(type(t)==turtle.Turtle, f"returned {type(t)}")
    def test_background(self):
        b = self.m.bgcolor()
        self.assertTrue(self.m.screen.bgcolor() == "blue" , f"the color is {self.m.screen.bgcolor()}")
    def test_size(self):
        s = self.m.screensize()
        self.assertTrue(self.m.screen.window_width() == SIZE)
        self.assertTrue(self.m.screen.window_height() == SIZE)

        # self.assertTrue(s[0] == SIZE, f"the x-dim is {s[0]}")
        # self.assertTrue(s[1] == SIZE, f"the y-dim is {s[1]}")

        # s = self.m.screensize()
        # self.assertTrue(self.m.screensize() == "SIZE , SIZE" , f"the size is {self.m.screensize()}")










if __name__=="__main__":
    unittest.main()
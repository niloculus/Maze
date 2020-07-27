import turtle
import unittest
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







if __name__=="__main__":
    unittest.main()
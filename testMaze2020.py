import turtle
import unittest
from Maze import Maze

class MazeTests(unittest.TestCase):
    def test_maze(self):
        m = Maze()
        self.assertTrue(type(m.screen) == turtle._Screen,"No Screen! type is" + str(type(m.screen)))
    def test_2(self):
        pass

if __name__=="__main__":
    unittest.main()
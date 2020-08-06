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
        self.assertTrue(self.m.screen.bgcolor() == "blue" , f"the color is {self.m.screen.bgcolor()}")
    def test_size(self):
        self.assertTrue(self.m.screen.window_width() == SIZE)
        self.assertTrue(self.m.screen.window_height() == SIZE)
    def testMatrixSize(self):
        self.assertTrue(len(self.m.matrix)==SIZE/20)
    def testReset(self):
        self.m.reset()
        self.assertTrue(self.m.matrix[0][0] == 0)
        p = self.m.t.pos()
        self.assertTrue(self.m.t.pos() == (-(SIZE / 2 - 20), SIZE / 2 - 20))
    def testSettingMatrixValues(self):
        m = Maze()
        m.reset()
        self.assertTrue(m.getMatrixValueAt(m.t.pos()) == 0)
        self.assertTrue(m.setMatrixValueAt(m.t.pos(), 1))
        self.assertTrue(self.m.matrix[0][0], 1)

    # def testdig(self):
    #     m=Maze()
    #     m.reset()
    #     r = m.dig(EAST)
    #     self.assertTrue(r ==(-160,180), "got " + str(r))

if __name__=="__main__":
    unittest.main()
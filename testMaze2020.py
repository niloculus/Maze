import turtle
import unittest
SIZE = 400

EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3
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
        self.assertTrue(self.m.screen.window_width() == SIZE*1.3)
        self.assertTrue(self.m.screen.window_height() == SIZE*1.3)
    def testMatrixSize(self):
        self.assertTrue(len(self.m.matrix)==SIZE/20)
    def testReset(self):
        self.m.reset()
        self.assertTrue(self.m.matrix[0][0] == 0)
        p = self.m.t.pos()
        self.assertTrue(self.m.t.pos() == (-(SIZE / 2 - 20), SIZE / 2 - 20))
    def testCoordinates(self):
        self.m.t.goto(-180, 180)
        self.m.t.stamp()
        self.m.t.goto(-180, -200)
        self.m.t.stamp()
        self.m.t.goto(200, -200)
        self.m.t.stamp()
        self.m.t.goto(200, 180)
        self.m.t.stamp()
        self.assertTrue((0, 0) == self.m.pos2index((-180, 180)), f"{self.m.pos2index((-180, 180))}")
        self.assertTrue((19, 19) == self.m.pos2index((200, -200)), f"{self.m.pos2index((200, -200))}")
    def testSettingMatrixValues(self):
        self.m.reset()
        value = self.m.getMatrixValueAt(self.m.t.position())
        self.assertTrue(0 == value)
        value = 1
        self.m.setMatrixValueAt(self.m.t.position(), value)
        self.assertEqual(self.m.matrix[0][0], 1)
        self.m.t.goto(-160, 180)
        value = self.m.getMatrixValueAt(self.m.t.position())
        self.assertTrue(1 == value)
        value = 0
        self.m.setMatrixValueAt(self.m.t.position(), value)
        self.assertEqual(self.m.matrix[0][1], 0)
        self.m.t.goto(200, -200)
        value = self.m.getMatrixValueAt(self.m.t.position())
        self.assertTrue(1 == value)
        value = 0
        self.m.setMatrixValueAt(self.m.t.position(), value)
        self.assertTrue(0 == value)
    def testSetMatrixValueAt(self):
        self.m.setMatrixValueAt(self.m.t.pos(), 1)
        self.assertTrue(self.m.matrix[0][0], 1)
        self.m.setMatrixValueAt(self.m.t.pos(), 0)
        self.assertTrue(self.m.matrix[0][0] == 0)

    def testDig(self):
        self.m.dig(EAST)
        self.assertEqual(self.m.t.pos(), (-160,180))
        self.assertTrue(self.m.matrix[1][0] == 0)
        self.m.dig(WEST)
        self.assertEqual(self.m.t.pos(), (-180,180))
        self.m.dig(NORTH)
        self.assertEqual(self.m.t.pos(), (-180, 180))
        self.m.dig(SOUTH)
        self.assertEqual(self.m.t.pos(), (-180, 160))


# def testdig(self):
    #     m=Maze()
    #     m.reset()
    #     r = m.dig(EAST)
    #     self.assertTrue(r ==(-160,180), "got " + str(r))

if __name__=="__main__":
    unittest.main()
import unittest
import util


TEST_INPUT_TEXT="""6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

class UtilTest(unittest.TestCase):

  def test_parse(self):
    points, instructions = util.parse(TEST_INPUT_TEXT)
    self.assertTrue((4, 1) in points)
    self.assertTrue((9, 0) in points)
    self.assertEqual(('y', 7), instructions[0])
    self.assertEqual(('x', 5), instructions[1])


  def test_fold(self):
    points, instructions = util.parse(TEST_INPUT_TEXT)
    util.fold(points, instructions[0])
    self.assertEqual(17, len(points))


if __name__ == '__main__':
    unittest.main()



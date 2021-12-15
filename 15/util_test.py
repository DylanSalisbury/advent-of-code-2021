import unittest
import util


TEST_INPUT_TEXT="""
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


class UtilTest(unittest.TestCase):

  def test_parse_grid(self):
    grid = util.parse_grid(TEST_INPUT_TEXT)
    self.assertEqual(1, grid[(9, 9)])
    self.assertEqual(8, grid[(9, 8)])
    self.assertEqual(1, grid[(8, 9)])

  def test_lowest_risk_path(self):
    grid = util.parse_grid(TEST_INPUT_TEXT)
    self.assertEqual(40, util.lowest_risk_path(grid))

  def test_expand_grid(self):
    grid = util.expand_grid(
      util.parse_grid(TEST_INPUT_TEXT))
    self.assertEqual(1, grid[(0, 0)])
    self.assertEqual(1, grid[(9, 9)])
    self.assertEqual(8, grid[(9, 8)])
    self.assertEqual(1, grid[(8, 9)])
    self.assertEqual(2, grid[(10, 0)])
    self.assertEqual(2, grid[(0, 10)])
    self.assertEqual(3, grid[(10, 10)])
    self.assertEqual(2, grid[(10, 0)])
    self.assertEqual(1, grid[(10, 45)])
    self.assertEqual(1, grid[(48, 48)])
    self.assertEqual(7, grid[(49, 48)])
    self.assertEqual(9, grid[(49, 49)])

  def test_part2_sample(self):
    grid = util.expand_grid(
      util.parse_grid(TEST_INPUT_TEXT))
    self.assertEqual(315, util.lowest_risk_path(grid))


if __name__ == '__main__':
    unittest.main()



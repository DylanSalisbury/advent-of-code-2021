import unittest
import util


TEST_INPUT_TEXT = (
"""
2199943210
3987894921
9856789892
8767896789
9899965678
""")

class UtilTest(unittest.TestCase):

  def test_parse_grid(self):
    grid = util.parse_grid(TEST_INPUT_TEXT)
    self.assertEqual(5, len(grid))
    self.assertEqual(10, len(grid[0]))
    self.assertEqual(1, grid[0][1])
    self.assertEqual(9, grid[4][0])

  def test_low_points(self):
    expected = {
      (0, 1),
      (0, 9),
      (2, 2),
      (4, 6)
    }
    self.assertEqual(expected, util.low_points(
      util.parse_grid(TEST_INPUT_TEXT)))

  def test_low_points_equality(self):
    # Neither of the 1 squares in the bottom left should be
    # treated as low points.
    TEST2_TEXT = ("""
2199943210
3987894921
9856789892
8767896789
1199965678
""")

    expected = {
      (0, 1),
      (0, 9),
      (2, 2),
      (4, 6)
    }
    self.assertEqual(expected, util.low_points(
      util.parse_grid(TEST2_TEXT)))
    
  def test_part1(self):
    self.assertEqual(15, util.part1(
      util.parse_grid(TEST_INPUT_TEXT)))

  def test_basins(self):
    expected_basin_sizes = (3, 9, 9, 14)
    grid = util.parse_grid(TEST_INPUT_TEXT)
    basins = util.basins(grid)
    sorted_basin_sizes = tuple(sorted(len(b) for b in basins))
    self.assertEqual(
      expected_basin_sizes, sorted_basin_sizes)
    self.assertEqual(
      1134,
      sorted_basin_sizes[-1]
      * sorted_basin_sizes[-2]
      * sorted_basin_sizes[-3])


if __name__ == '__main__':
    unittest.main()

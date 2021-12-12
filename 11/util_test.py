import unittest
import util


TEST_INPUT_TEXT = ("""
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""")


class UtilTest(unittest.TestCase):

  def test_step(self):
    grid = util.parse_grid(TEST_INPUT_TEXT)
    util.print_grid(grid)
    self.assertEqual(0, util.step(grid))
    self.assertEqual(35, util.step(grid))
    total_flashes = 35
    for _ in range(98):
      total_flashes += util.step(grid)
    self.assertEqual(1656, total_flashes)


if __name__ == '__main__':
    unittest.main()

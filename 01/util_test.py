import unittest
import util


TEST_INPUT = (
  199,
  200,
  208,
  210,
  200,
  207,
  240,
  269,
  260,
  263)


class UtilTest(unittest.TestCase):

  def test_count_increases(self):
    self.assertEqual(7, util.count_increases(
      TEST_INPUT))

  def test_window_increases(self):
    self.assertEqual(5, util.window_increases(
      TEST_INPUT))


if __name__ == '__main__':
    unittest.main()



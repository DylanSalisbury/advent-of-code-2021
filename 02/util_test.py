import unittest
import util


TEST_INPUT = (
  'forward 5',
  'down 5',
  'forward 8',
  'up 3',
  'down 8',
  'forward 2')


class UtilTest(unittest.TestCase):

  def test_nav(self):
    self.assertEqual((15, 10), util.nav(TEST_INPUT))

  def test_nav2(self):
    self.assertEqual((15, 60), util.nav2(TEST_INPUT))


if __name__ == '__main__':
    unittest.main()



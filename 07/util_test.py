import unittest
import util


TEST_INPUT=(16,1,2,0,4,2,7,1,2,14)


class UtilTest(unittest.TestCase):

  def test_min_fuel(self):
    self.assertEqual(37, util.min_fuel(TEST_INPUT))
    self.assertEqual(168, util.min_fuel(TEST_INPUT, True))


if __name__ == '__main__':
    unittest.main()



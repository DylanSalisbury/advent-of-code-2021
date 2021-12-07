import unittest
import util


TEST_INPUT = (3,4,3,1,2)
PART1_AFTER_3_DAYS = (0,1,0,5,6,7,8)


class UtilTest(unittest.TestCase):

  def test_part1_produce(self):
    self.assertEqual(
      5934, util.part1_produce(TEST_INPUT, 80))


if __name__ == '__main__':
    unittest.main()



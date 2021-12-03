import unittest
import util


class UtilTest(unittest.TestCase):

  def test_func(self):
    self.assertEqual(327, util.func(327))


if __name__ == '__main__':
    unittest.main()



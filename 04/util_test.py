import unittest
import util

TEST_BOARD_TEXT = (
"""14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""")


class UtilTest(unittest.TestCase):

  def test_board_horizontal(self):
    TEST_NUMBERS_WITHOUT_WINNING = (
      7,4,9,5,11,17,23,2,0,14,21)

    TEST_WINNING_NUMBER = 24

    b = util.Board(TEST_BOARD_TEXT)
    self.assertFalse(b.won())
    for number in TEST_NUMBERS_WITHOUT_WINNING:
      b.mark(number)
      self.assertFalse(b.won())
    b.mark(TEST_WINNING_NUMBER)
    self.assertTrue(b.won())
    self.assertEqual(188, b.unmarked_sum())
    
  def test_board_vertical(self):
    TEST_NUMBERS_WITHOUT_WINNING = (
      7,4,9,5,11,17,23,2,0,14,21,19)

    TEST_WINNING_NUMBER = 20

    b = util.Board(TEST_BOARD_TEXT)
    self.assertFalse(b.won())
    for number in TEST_NUMBERS_WITHOUT_WINNING:
      b.mark(number)
      self.assertFalse(b.won())
    b.mark(TEST_WINNING_NUMBER)
    self.assertTrue(b.won())
    self.assertEqual(
      188+24-19-20, b.unmarked_sum())


if __name__ == '__main__':
    unittest.main()



import unittest
import util


TEST_INPUT = (
  ((0,9), (5,9)),
  ((8,0), (0,8)),
  ((9,4), (3,4)),
  ((2,2), (2,1)),
  ((7,0), (7,4)),
  ((6,4), (2,0)),
  ((0,9), (2,9)),
  ((3,4), (1,4)),
  ((0,0), (8,8)),
  ((5,5), (8,2)))


ALIGNED_ONLY_CLOUDS = (
  ((0,9), (5,9)),
  ((9,4), (3,4)),
  ((2,2), (2,1)),
  ((7,0), (7,4)),
  ((0,9), (2,9)),
  ((3,4), (1,4)))



class UtilTest(unittest.TestCase):

  def test_filter_aligned(self):
    self.assertEqual(
      ALIGNED_ONLY_CLOUDS,
      util.filter_aligned(TEST_INPUT))


  def test_overlapping_cells(self):
    c = util.overlapping_cells(ALIGNED_ONLY_CLOUDS)
    self.assertEqual(5, len(c))
    self.assertTrue((3, 4) in c)
    self.assertFalse((2, 4) in c)
    self.assertFalse((4, 4) in c)

    c = util.overlapping_cells(TEST_INPUT)
    self.assertEqual(12, len(c))

if __name__ == '__main__':
    unittest.main()



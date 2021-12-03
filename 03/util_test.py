import unittest
import util


TEST_INPUT = (
  "00100",
  "11110",
  "10110",
  "10111",
  "10101",
  "01111",
  "00111",
  "11100",
  "10000",
  "11001",
  "00010",
  "01010")


class UtilTest(unittest.TestCase):

  def test_bits_to_int(self):
    self.assertEqual(
      22,
      util.bits_to_int(util.string_to_bits('10110')))
    self.assertEqual(
      9,
      util.bits_to_int(util.string_to_bits('01001')))

  def test_gamma_epsilon(self):
    self.assertEqual(
      (22, 9), util.gamma_epsilon(TEST_INPUT))

  def test_oxygen_co2(self):
    self.assertEqual(
      (23, 10), util.oxygen_co2(TEST_INPUT))


if __name__ == '__main__':
    unittest.main()

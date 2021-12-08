import unittest
import util


TEST_LINE = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'


class UtilTest(unittest.TestCase):

  def test_part1(self):
    self.assertEqual(26, util.part1('test_input.txt'))

  def test_map_wires(self):
    m = util.map_wires(TEST_LINE)
    self.assertEqual('d', m['a'])
    self.assertEqual('e', m['b'])
    self.assertEqual('a', m['c'])
    self.assertEqual('f', m['d'])
    self.assertEqual('g', m['e'])
    self.assertEqual('b', m['f'])
    self.assertEqual('c', m['g'])

  def test_solve_line(self):
    self.assertEqual(5353, util.solve_line(TEST_LINE))

  def test_part2(self):
    self.assertEqual(61229, util.part2('test_input.txt'))


if __name__ == '__main__':
    unittest.main()



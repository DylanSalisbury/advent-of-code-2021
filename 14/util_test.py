import unittest
import util


TEST_INPUT_TEXT="""NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

class UtilTest(unittest.TestCase):

  def test_parse_input(self):
    s, rules = util.parse_input(TEST_INPUT_TEXT)
    self.assertEqual('NNCB', s)
    self.assertEqual('N', rules['CC'])
    self.assertEqual('C', rules['CN'])

    
  def test_step(self):
    s = ['']
    s[0], rules = util.parse_input(TEST_INPUT_TEXT)
    self.assertEqual('NNCB', s[-1])
    s.append(util.step(s[-1], rules))
    self.assertEqual('NCNBCHB', s[-1])
    s.append(util.step(s[-1], rules))
    self.assertEqual('NBCCNBBBCBHCB', s[-1])
    s.append(util.step(s[-1], rules))
    self.assertEqual('NBBBCNCCNBBNBNBBCHBHHBCHB', s[-1])
    s.append(util.step(s[-1], rules))
    self.assertEqual('NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB', s[-1])

    
  def test_diff(self):
    s, rules = util.parse_input(TEST_INPUT_TEXT)
    for _ in range(10):
      s = util.step(s, rules)
    self.assertEqual(1588, util.diff(s))

    
  def test_solve2(self):
    s, rules = util.parse_input(TEST_INPUT_TEXT)
    self.assertEqual(1588, util.solve2(s, rules, 10))
    self.assertEqual(2188189693529, util.solve2(s, rules, 40))


if __name__ == '__main__':
    unittest.main()



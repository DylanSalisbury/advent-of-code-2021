import unittest
import util


SMALL_INPUT_TEXT="""
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""


TEST_INPUT_TEXT="""
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

class UtilTest(unittest.TestCase):

  def test_parse_input(self):
    edges = util.parse_input(TEST_INPUT_TEXT)
    self.assertEqual(set(('start', 'sa', 'HN', 'dc')), edges['kj'])
    self.assertEqual(set(('start', 'end', 'dc', 'kj')), edges['HN'])

  def test_find_paths(self):
    paths = util.find_paths(util.parse_input(TEST_INPUT_TEXT))
    self.assertEqual(19, len(paths))

  def test_find_paths_small(self):
    paths = util.find_paths_v2(util.parse_input(SMALL_INPUT_TEXT))
    self.assertEqual(36, len(paths))

  def test_find_paths(self):
    paths = util.find_paths_v2(util.parse_input(TEST_INPUT_TEXT))
    self.assertEqual(103, len(paths))

if __name__ == '__main__':
    unittest.main()

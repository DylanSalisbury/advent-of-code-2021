import unittest
import util


class UtilTest(unittest.TestCase):

  def test_error_score(self):
    TEST_CASES=(
      (0, '()'),
      (0, '[]'),
      (0, '(<>)'),
      (0, '{()()()}'),

      (1197, '{([(<{}[<>[]}>{[]{[(<()>'),
      (3, '[[<[([]))<([[{}[[()]]]'),
      (57, '[{[{({}]{}}([{[{{{}}([]')
    )
    for test_case in TEST_CASES:
      self.assertEqual(test_case[0], util.error_score(test_case[1]))

  def test_completion_score(self):
    TEST_CASES=(
      (288957, '[({(<(())[]>[[{[]{<()<>>'),
      (5566, '[(()[<>])]({[<{<<[]>>(')
    )
    for test_case in TEST_CASES:
      self.assertEqual(test_case[0], util.completion_score(test_case[1]))


if __name__ == '__main__':
    unittest.main()



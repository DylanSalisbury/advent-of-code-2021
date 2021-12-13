import unittest
import part2


class Part2Test(unittest.TestCase):

  def test_solve(self):
    with open('expected_output.txt') as f:
      self.assertEqual(f.read(), part2.solve('input.txt'))


if __name__ == '__main__':
    unittest.main()



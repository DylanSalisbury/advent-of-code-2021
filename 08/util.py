"""Helper functions."""
import re


INPUT_WIRES_BY_DIGIT = (
  set(('a', 'b', 'c', 'e', 'f', 'g')),
  set(('c', 'f')),
  set(('a', 'c', 'd', 'e', 'g')),
  set(('a', 'c', 'd', 'f', 'g')),
  set(('b', 'c', 'd', 'f')),
  set(('a', 'b', 'd', 'f', 'g')),
  set(('a', 'b', 'd', 'e', 'f', 'g')),
  set(('a', 'c', 'f')),
  set(('a', 'b', 'c', 'd', 'e', 'f', 'g')),
  set(('a', 'b', 'c', 'd', 'f', 'g')))


def part1(input_path):
  all_digits = []
  with open(input_path) as f:
    for s in f:
      right_part = s.rstrip().split('|')[1]
      right_digits = right_part.split(' ')[1:]
      all_digits.extend(right_digits)
  special_digits = tuple(filter(
    lambda d: len(d) in set((2, 4, 3, 7)), all_digits))
  return len(special_digits)


def map_wires(line):
  result = dict()
  # We probably aren't supposed to need the digits to the right of the
  # |, but let's capture them just in case.
  digits_text = ''.join(line.split('| ')).split(' ')
  digits_sets = tuple(set(t) for t in digits_text)
  digits_by_length = []
  for _ in range(9):
    digits_by_length.append([])
  for d in digits_sets:
    digits_by_length[len(d)].append(d)

  result['a'] = tuple(filter(
    lambda d: not d in set.union(*digits_by_length[2]),
    digits_by_length[3][0]
  ))[0]

  b_or_d = set(filter(
    lambda d: not d in set.union(*digits_by_length[3]),
    digits_by_length[4][0]
  ))

  result['b'] = tuple(filter(
    lambda d: not d in set.intersection(*digits_by_length[5]),
    b_or_d
  ))[0]

  result['d'] = tuple(filter(
    lambda d: d != result['b'],
    b_or_d
  ))[0]

  digit_five_inputs = tuple(filter(
    lambda s: result['a'] in s and result['b'] in s and result['d'] in s,
    digits_by_length[5]
  ))[0]

  f_or_g = set(filter(
    lambda d: not d in set((result['a'], result['b'], result['d'])),
    digit_five_inputs
  ))

  result['f'] = tuple(filter(
    lambda d: d in digits_by_length[3][0],
    f_or_g
  ))[0]

  result['g'] = tuple(filter(
    lambda d: d != result['f'],
    f_or_g
  ))[0]

  result['c'] = tuple(filter(
    lambda d: d != result['f'],
    digits_by_length[2][0],
  ))[0]

  result['e'] = tuple(filter(
    lambda d: not d in result.values(),
    digits_by_length[7][0],
  ))[0]
  
  return result


def solve_line(line):
  wire_map = {v: k for k, v in map_wires(line).items()}
  result_input_wires_strings = line.split('| ')[1].split(' ')
  result_output_wires_sets = tuple(
    set(map(lambda d: wire_map[d], tuple(s)))
    for s in result_input_wires_strings)
  digits = tuple(INPUT_WIRES_BY_DIGIT.index(s) for s in result_output_wires_sets)
  return digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]


def part2(input_path):
  with open(input_path) as f:
    return sum(tuple(solve_line(s.rstrip()) for s in f))

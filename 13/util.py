"""Helper functions."""
import re


def parse(s):
  points_text, instructions_text = s.split('\n\n')
  points = set()
  for a in points_text.split('\n'):
    c = a.split(',')
    points.add((int(c[0]), int(c[1])))
  instructions = []
  for i in instructions_text.rstrip().split('\n'):
    m = re.match(r'fold along (.)=(\d+)', i)
    instructions.append((m.group(1), int(m.group(2))))
  return (points, tuple(instructions))


def fold(points, instruction):
  if instruction[0] == 'x':
    fold_index = 0
    notfold_index = 1
  else:
    fold_index = 1
    notfold_index = 0
  for p in tuple(points):
    if p[fold_index] <= instruction[1]:
      continue
    points.remove(p)
    newp = list(p)
    newp[fold_index] = 2 * instruction[1] - p[fold_index]
    points.add(tuple(newp))  # This is where duplicates get ignored

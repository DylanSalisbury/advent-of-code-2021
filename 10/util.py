"""Helper functions."""

def scores(line):
  pairs = { '(': ')', '[': ']', '{': '}', '<': '>' }
  error_points = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
  completion_points = { '(': 1, '[': 2, '{': 3, '<': 4 }
  openers = pairs.keys()
  
  stack = []
  
  for c in line:
    if c in openers:
      stack.append(c)
      continue
    if len(stack) == 0 or pairs[stack.pop()] != c:
      return (error_points[c], 0)

  score = 0
  while len(stack) > 0:
    score = score * 5 + completion_points[stack.pop()]

  return (0, score)


def error_score(line):
  return scores(line)[0]


def completion_score(line):
  return scores(line)[1]

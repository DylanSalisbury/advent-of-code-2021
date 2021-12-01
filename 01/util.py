"""Helper functions."""

def count_increases(depths):
  result = 0
  for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
      result += 1

  return result


def window_increases(depths):
  result = 0
  for i in range(1, len(depths) - 2):
    if sum(depths[i:i+3]) > sum(depths[i-1:i+2]):
      result += 1

  return result

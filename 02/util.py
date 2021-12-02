"""Helper functions."""

def nav(directions):
  horizontal = 0
  depth = 0
  for s in directions:
    action, amount = s.split(' ')
    amount = int(amount)
    if action == 'forward':
      horizontal += amount
    elif action == 'down':
      depth += amount
    elif action == 'up':
      depth -= amount
    else:
      raise ValueError(
        'Unknown action "+' + action + '"')

  return (horizontal, depth)


def nav2(directions):
  horizontal = 0
  depth = 0
  aim = 0
  for s in directions:
    action, amount = s.split(' ')
    amount = int(amount)
    if action == 'forward':
      horizontal += amount
      depth += aim * amount
    elif action == 'down':
      aim += amount
    elif action == 'up':
      aim -= amount
    else:
      raise ValueError(
        'Unknown action "+' + action + '"')

  return (horizontal, depth)

"""Helper functions."""


def parse_grid(n):
  result = dict()
  row = 0
  for line in n.split('\n'):
    if len(line) > 0:
      for col in range(len(line)):
        result[row, col] = int(line[col])
      row += 1
  return result


def print_grid(grid):
  pos_ordered = sorted(grid.keys())
  cur_row = pos_ordered[0][0]
  for pos in pos_ordered:
    if pos[0] != cur_row:
      print('')
    print(str(grid[pos]), end='')
    cur_row = pos[0]
  print('\n')


def neighbors(grid, pos):
  row = pos[0]
  col = pos[1]
  result = (
    (row-1, col-1),
    (row-1, col),
    (row-1, col+1),
    (row, col-1),
    (row, col+1),
    (row+1, col-1),
    (row+1, col),
    (row+1, col+1)
  )
  result = tuple(filter(lambda coord: coord in grid, result))
  return result


def step(grid):
  num_flashes = 0
  cells_to_increase = grid.keys()
  while (len(cells_to_increase) > 0):
    next_cells_to_increase = []
    for pos in cells_to_increase:
      grid[pos] += 1
      if grid[pos] == 10:
        num_flashes += 1
        next_cells_to_increase.extend(neighbors(grid, pos))
    cells_to_increase = next_cells_to_increase

  for pos in grid.keys():
    if (grid[pos] >= 10):
      grid[pos] = 0

  return num_flashes

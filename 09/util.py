"""Helper functions."""
from collections import defaultdict


def parse_grid(n):
  result = []
  for line in n.split('\n'):
    if len(line) > 0:
      result.append(list(int(c) for c in line))
  return result


def low_points(grid):
  result = set()
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      v = grid[row][col]
      if row > 0 and grid[row-1][col] <= v:
        continue
      if row < len(grid)-1 and grid[row+1][col] <= v:
        continue
      if col > 0 and grid[row][col-1] <= v:
        continue
      if col < len(grid[0])-1 and grid[row][col+1] <= v:
        continue
      result.add((row, col))
  return result

def part1(grid):
  return sum(1+grid[p[0]][p[1]] for p in low_points(grid))

def print_grid(grid):
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      v = grid[row][col]
      s = " "
      if v is not None:
        s = str(v)
      print(s, end='')
    print("")

def basins(grid):
  # Map of basin ID number (starting from 1 but **NO RELATION** to the
  # input numbers) to set of (col, row) coordinates.
  basins = defaultdict(lambda: set())
  next_basin_id = 1
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] == 9:
        grid[row][col] = None
        continue

      curr_basin_id = None

      if col > 0:
        left_basin = grid[row][col-1]
        if left_basin:
          curr_basin_id = left_basin

      if row > 0:
        above_basin = grid[row-1][col]
        if above_basin:
          if not curr_basin_id:
            curr_basin_id = above_basin
          elif curr_basin_id != above_basin:
            # Join those two basins
            # print("joining basin " + str(above_basin) + " into " + str(curr_basin_id))
            for pos in basins.pop(above_basin):
              grid[pos[0]][pos[1]] = curr_basin_id
              basins[curr_basin_id].add(pos)

      if not curr_basin_id:
        curr_basin_id = next_basin_id
        next_basin_id += 1

      grid[row][col] = curr_basin_id
      basins[curr_basin_id].add((row,col))

      # print("Set [%d,%d] to %d" % (row, col, curr_basin_id))
      # print_grid(grid)
      # print("")

  return tuple(basins.values())

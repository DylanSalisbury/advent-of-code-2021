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


def lowest_risk_path(grid):
  costs = dict()
  rev_points = tuple(reversed(sorted(grid.keys())))
  costs[rev_points[0]] = 0
  for p in rev_points[1:]:
    right = (p[0], p[1]+1)
    down = (p[0]+1, p[1])
    neighbor_costs = []
    if right in costs:
      neighbor_costs.append(grid[right] + costs[right])
    if down in costs:
      neighbor_costs.append(grid[down] + costs[down])
    costs[p] = min(neighbor_costs)
  result = costs[(0, 0)]
  # This part is not covered properly by tests,
  # and takes 2 minutes to run on full input file :(
  while True:
    print("Trying to improve result...")
    old_result = result
    improved, new_costs = improve(costs, grid)
    if not improved:
      return result
    result = new_costs[(0, 0)]
    costs = new_costs


def improve(old_costs, grid):
  improved = False
  costs = dict()
  rev_points = tuple(reversed(sorted(grid.keys())))
  costs[rev_points[0]] = 0
  for p in rev_points[1:]:
    neighbors = (
      (p[0], p[1]+1),
      (p[0]+1, p[1]),
      (p[0], p[1]-1),
      (p[0]-1, p[1]))
    neighbor_costs = []
    for n in neighbors:
      if n in old_costs:
        neighbor_costs.append(grid[n] + old_costs[n])
      if n in costs:
        neighbor_costs.append(grid[n] + costs[n])
    costs[p] = min(neighbor_costs)
    if costs[p] < old_costs[p]:
      improved = True
  return improved, costs
  

def expand_grid(grid):
  corner = max(grid.keys())
  result = dict()
  for k in grid:
    for r in range(5):
      for c in range(5):
        v = 1 + ((grid[k] + r + c) - 1) % 9
        p = (k[0] + r * (1 + corner[0]), k[1] + c * (1 + corner[1]))
        result[p] = v
  return result


def func(n):
  return n

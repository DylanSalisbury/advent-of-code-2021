import util


def solve(input_path):
  with open(input_path) as f:
    grid = util.parse_grid(f.read())
    target = len(grid.keys())
    steps = 1
    while (util.step(grid) != target):
      steps += 1
    return steps


if __name__ == '__main__':
    print(solve('input.txt'))

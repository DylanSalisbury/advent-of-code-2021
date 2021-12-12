import util


def solve(input_path):
  with open(input_path) as f:
    grid = util.parse_grid(f.read())
    result = 0
    for _ in range(100):
      result += util.step(grid)
    return result


if __name__ == '__main__':
    print(solve('input.txt'))

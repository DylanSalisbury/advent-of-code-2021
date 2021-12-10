import util


def solve(input_path):
  with open(input_path) as f:
    grid = util.parse_grid(f.read())
    return util.part1(grid)


if __name__ == '__main__':
    print(solve('input.txt'))

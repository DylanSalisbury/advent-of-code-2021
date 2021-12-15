import util


def solve(input_path):
  with open(input_path) as f:
    return util.lowest_risk_path(
      util.expand_grid(
        util.parse_grid(f.read())))



if __name__ == '__main__':
    print(solve('input.txt'))

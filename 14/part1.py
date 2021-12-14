import util


def solve(input_path):
  with open(input_path) as f:
    s, rules = util.parse_input(f.read())
    for _ in range(10):
      s = util.step(s, rules)
    return util.diff(s)


if __name__ == '__main__':
    print(solve('input.txt'))

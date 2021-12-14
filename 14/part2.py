import util


def solve(input_path):
  with open(input_path) as f:
    s, rules = util.parse_input(f.read())
    return util.solve2(s, rules, 40)


if __name__ == '__main__':
    print(solve('input.txt'))

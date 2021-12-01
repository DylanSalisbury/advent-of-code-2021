import util


def solve(input_path):
  with open(input_path) as f:
    depths = [int(s.rstrip()) for s in f]
    return util.count_increases(depths)


if __name__ == '__main__':
    print(solve('input.txt'))

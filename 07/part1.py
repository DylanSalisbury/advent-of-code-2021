import util


def solve(input_path):
  with open(input_path) as f:
    return util.min_fuel(int(s) for s in f.readline().rstrip().split(','))


if __name__ == '__main__':
    print(solve('input.txt'))

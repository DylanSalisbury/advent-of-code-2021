import util


def solve(input_path):
  with open(input_path) as f:
    return sum(util.error_score(s.rstrip()) for s in f)


if __name__ == '__main__':
    print(solve('input.txt'))

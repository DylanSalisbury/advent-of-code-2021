import util


def solve(input_path):
  with open(input_path) as f:
    p, i = util.parse(f.read())
    util.fold(p, i[0])
    return len(p)


if __name__ == '__main__':
    print(solve('input.txt'))

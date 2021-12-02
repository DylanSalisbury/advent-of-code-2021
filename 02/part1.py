import util


def solve(input_path):
  with open(input_path) as f:
    h, d = util.nav(
      [s.rstrip() for s in f])
    
    return h * d


if __name__ == '__main__':
    print(solve('input.txt'))

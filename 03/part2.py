import util


def solve(input_path):
  with open(input_path) as f:
    oxygen, co2 = util.oxygen_co2(
      s.rstrip() for s in f)
    return oxygen * co2


if __name__ == '__main__':
    print(solve('input.txt'))

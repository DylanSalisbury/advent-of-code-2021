import util


def solve(input_path):
  with open(input_path) as f:
    input = (int(s) for s in
             f.readline().rstrip().split(','))
    return util.part1_produce(input, 256)


if __name__ == '__main__':
    print(solve('input.txt'))

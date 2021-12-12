import util


def solve(input_path):
  with open(input_path) as f:
    return len(util.find_paths_v2(util.parse_input(f.read())))


if __name__ == '__main__':
    print(solve('input.txt'))

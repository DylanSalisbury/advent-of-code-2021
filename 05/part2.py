import util


def solve(input_path):
  with open(input_path) as f:
    clouds = util.parse_clouds(f)
    return len(util.overlapping_cells(clouds))


if __name__ == '__main__':
    print(solve('input.txt'))

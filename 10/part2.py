import util


def solve(input_path):
  with open(input_path) as f:
    line_points = tuple(util.completion_score(s.rstrip()) for s in f)
    positive_points = tuple(filter(lambda s: s > 0, line_points))
    return sorted(positive_points)[int(len(positive_points) / 2)]


if __name__ == '__main__':
    print(solve('input.txt'))

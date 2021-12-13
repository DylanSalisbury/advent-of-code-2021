import util


def solve(input_path):
  with open(input_path) as f:
    points, instructions = util.parse(f.read())
    for i in instructions:
      util.fold(points, i)
    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)
    grid = []
    for y in range(1 + max_y):
      grid.append([' '] * (1 + max_x))
    for p in points:
      grid[p[1]][p[0]] = '#'
    result_lines = []
    for y in range(len(grid)):
      result_lines.append(''.join(grid[y]))
    result_lines.append('')
    return '\n'.join(result_lines)


if __name__ == '__main__':
    print(solve('input.txt'))

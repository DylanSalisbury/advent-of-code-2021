import util


def solve(input_path):
  with open(input_path) as f:
    grid = util.parse_grid(f.read())
    basins = util.basins(grid)
    sorted_basin_sizes = tuple(sorted(len(b) for b in basins))
    return (sorted_basin_sizes[-1]
      * sorted_basin_sizes[-2]
      * sorted_basin_sizes[-3])


if __name__ == '__main__':
    print(solve('input.txt'))

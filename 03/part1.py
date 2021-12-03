import util


def solve(input_path):
  with open(input_path) as f:
    gamma, epsilon = util.gamma_epsilon(
      s.rstrip() for s in f)
    return gamma * epsilon


if __name__ == '__main__':
    print(solve('input.txt'))

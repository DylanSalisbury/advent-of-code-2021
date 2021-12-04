import util


def solve(input_path):
  (numbers, boards) = util.read_input(input_path)
      
  for n in numbers:
    for b in boards:
      b.mark(n)
      if b.won():
        return n * b.unmarked_sum()


if __name__ == '__main__':
    print(solve('input.txt'))

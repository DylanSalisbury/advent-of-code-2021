import util


def solve(input_path):
  (numbers, boards) = util.read_input(input_path)

  for n in numbers:
    # list(boards) copies boards because the
    # contents of the loop may remove an item
    # from boards, causing the iteration to have
    # unexpected behavior.
    for b in list(boards):
      b.mark(n)
      if b.won():
        boards.remove(b)
        if len(boards) == 0:
          return n * b.unmarked_sum()


if __name__ == '__main__':
    print(solve('input.txt'))

"""Helper functions."""


class Board:
  def __init__(self, text):
    self.has_won = False
    self.number_rows = [
      (int(rows_text[0:2]),
       int(rows_text[3:5]),
       int(rows_text[6:8]),
       int(rows_text[9:11]),
       int(rows_text[12:14])) for rows_text in text.split('\n')]
    self.unmarked_set = set()
    for row in self.number_rows:
      for n in row:
        self.unmarked_set.add(n)
    self.marked_coords = set()  # row,col pairs
    self.number_coords = dict()
    for r in range(len(self.number_rows)):
      for c in range(len(self.number_rows[0])):
        n = self.number_rows[r][c]
        self.number_coords[n] = (r, c)

  def mark(self, number):
    if number in self.unmarked_set:
      self.unmarked_set.remove(number)
      (r, c) = self.number_coords[number]
      self.marked_coords.add( (r, c) )
      w = True
      for r2 in range(len(self.number_rows)):
        if not (r2, c) in self.marked_coords:
          w = False
      if w:
        self.has_won = True
      w = True
      for c2 in range(len(self.number_rows[0])):
        if not (r, c2) in self.marked_coords:
          w = False
      if w:
        self.has_won = True

  def won(self):
    return self.has_won

  def unmarked_sum(self):
    return sum(self.unmarked_set)


def read_input(input_path):
  numbers = []
  boards = []
  with open(input_path) as f:
    numbers = [
      int(s) for s in
      f.readline().rstrip().split(',')]
    while len(f.readline()) > 0:
      t = (
        f.readline() + 
        f.readline() + 
        f.readline() + 
        f.readline() + 
        f.readline()).rstrip()
      boards.append(Board(t))

  return (numbers, boards)


"""Helper functions."""
from collections import defaultdict
import re

def parse_input(i):
  s, rules_text = i.split('\n\n')
  rules = dict()
  for r in rules_text.rstrip().split('\n'):
    m = re.match(r'(..) -> (.)', r)
    rules[m.group(1)] = m.group(2)
  return s, rules


def step(s, rules):
  result_chars = []
  result_chars.append(s[0])
  for i in range(0, len(s)-1, 1):
    result_chars.append(rules[s[i:i+2]])
    result_chars.append(s[i+1])

  return ''.join(result_chars)


def diff(s):
  d = defaultdict(lambda: 0)
  for c in s:
    d[c] += 1
  
  return max(d.values()) - min(d.values())


def solve2(s, rules, iters):
  pairs_count = defaultdict(lambda: 0)
  for i in range(len(s)-1):
    pairs_count[s[i:i+2]] += 1

  for _ in range(iters):
    new_pairs = defaultdict(lambda: 0)
    for p in tuple(pairs_count.keys()):
      c = rules[p]
      p1 = p[0] + c
      p2 = c + p[1]
      new_pairs[p1] += pairs_count[p]
      new_pairs[p2] += pairs_count[p]
    pairs_count = new_pairs
  c = defaultdict(lambda: 0)
  for p in tuple(pairs_count.keys()):
    c[p[0]] += pairs_count[p]
    c[p[1]] += pairs_count[p]

  # But now they're all double counted except for ..
  c[s[0]] += 1
  c[s[-1]] += 1

  return int((max(c.values()) - min(c.values())) / 2)

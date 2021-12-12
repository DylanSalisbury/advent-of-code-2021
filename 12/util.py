"""Helper functions."""
import re
from collections import defaultdict


def parse_input(s):
  result = defaultdict(lambda: set())
  for line in s.split('\n'):
    if len(line) == 0:
      continue
    a = line.split('-')
    result[a[0]].add(a[1])
    result[a[1]].add(a[0])
  return result


def all_lowercase(s):
  return bool(re.match(r'^[a-z]+$', s))


def find_paths(edges):
  return recursive_paths(edges, tuple(['start']))
  

def recursive_paths(edges, path_so_far):
  result = []
  for next_cave in edges[path_so_far[-1]]:
    if next_cave == 'end':
      result.append(path_so_far + tuple([next_cave]))
      continue
    if all_lowercase(next_cave) and next_cave in path_so_far:
      continue
    result.extend(recursive_paths(edges, (path_so_far + tuple([next_cave]))))
  return tuple(result)

def find_paths_v2(edges):
  return recursive_paths_v2(edges, tuple(['start']), False)
  

def recursive_paths_v2(edges, path_so_far, already_doubled):
  result = []
  for next_cave in edges[path_so_far[-1]]:
    now_doubled = already_doubled
    if next_cave == 'end':
      result.append(path_so_far + tuple([next_cave]))
      continue
    if all_lowercase(next_cave) and next_cave in path_so_far:
      if next_cave == 'start':
        continue
      if already_doubled:
        continue
      now_doubled = True
    result.extend(recursive_paths_v2(
      edges, (path_so_far + tuple([next_cave])), now_doubled))
  return tuple(result)

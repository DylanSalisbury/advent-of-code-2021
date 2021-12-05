"""Helper functions."""
import re


def filter_aligned(clouds):
  return tuple(filter(
    lambda cloud: (
      cloud[0][0] == cloud[1][0] or
      cloud[0][1] == cloud[1][1]),
    clouds))


def overlapping_cells(clouds):
  p = set()  # populated cells
  o = set()  # overlapping cells
  for cloud in clouds:
    cloud = sorted(cloud)
    cloud_points = []
    if cloud[0][0] == cloud[1][0]:
      x = cloud[0][0]
      for y in range(cloud[0][1], cloud[1][1]+1):
        cloud_points.append( (x, y) )
    elif cloud[0][1] == cloud[1][1]:
      y = cloud[0][1]
      for x in range(cloud[0][0], cloud[1][0]+1):
        cloud_points.append( (x, y) )
    else:
      # Cloud was sorted above, so x vals increase
      x = cloud[0][0]
      if cloud[0][1] < cloud[1][1]:
        r = range(cloud[0][1], cloud[1][1]+1)
      else:
        r = range(cloud[0][1], cloud[1][1]-1, -1)
      for y in r:
        cloud_points.append( (x, y) )
        x += 1

    for point in cloud_points:
      if point in p:
        o.add(point)
      else:
        p.add(point)

  return o


def parse_clouds(f):
    clouds_text = tuple(s.rstrip() for s in f)
    exp = r'(\d+),(\d+) -> (\d+),(\d+)'
    fours = tuple(
      map(
        lambda t: (
          re.match(exp, t).groups()),
        clouds_text))
    return tuple(
      map(lambda f: (
        (int(f[0]), int(f[1])),
        (int(f[2]), int(f[3]))),
          fours))

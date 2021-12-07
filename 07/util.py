"""Helper functions."""

def min_fuel(inputs, cumulative_fuel=False):
  initial_positions = sorted(inputs)
  right_fuel_needed = [0] * (1 + initial_positions[-1])
  passed = 0
  step_cost = 0
  for i in range(0, 1 + initial_positions[-1]):
    if i > 0:
      if cumulative_fuel:
        step_cost += passed
        right_fuel_needed[i] = right_fuel_needed[i-1] + step_cost
      else:
        right_fuel_needed[i] = right_fuel_needed[i-1] + passed
    while passed < len(initial_positions) and initial_positions[passed] == i:
      passed += 1

  left_fuel_needed = [0] *  (1 + initial_positions[-1])
  passed = 0
  step_cost = 0
  for i in range(initial_positions[-1], -1, -1):
    if i < initial_positions[-1]:
      if cumulative_fuel:
        step_cost += passed
        left_fuel_needed[i] = left_fuel_needed[i+1] + step_cost
      else:
        left_fuel_needed[i] = left_fuel_needed[i+1] + passed
    while passed < len(initial_positions) and initial_positions[-1-passed] == i:
      passed += 1

  fuel_needed = [left_fuel_needed[p] + right_fuel_needed[p] for p in range(1 + initial_positions[-1])]
  return min(fuel_needed)

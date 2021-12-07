"""Helper functions."""

def part1_produce(input_fish, days):
  state = [0] * 9
  
  for t in input_fish:
    state[t] += 1
    
  for _ in range(days):
    z = state[0]
    for s in range(8):
      state[s] = state[s+1]
    state[6] += z
    state[8] = z
      
  return sum(state)

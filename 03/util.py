"""Helper functions."""


def string_to_bits(s):
  return tuple([int(c) for c in s])


def bits_to_int(bits):
  result = 0
  for bit in bits:
    result *= 2
    result += bit

  return result


def gamma_epsilon(strings):
  gamma_bits, epsilon_bits = (
    bits_list_to_gamma_epsilon_bits(
      string_to_bits(s) for s in strings))

  return(
    bits_to_int(gamma_bits),
    bits_to_int(epsilon_bits))


def bits_list_to_gamma_epsilon_bits(bits_list):
  num_bits = None
  how_many_more_ones = None
  for bits in bits_list:
    if not num_bits:
      # Assume all input strings have the same length.
      num_bits = len(bits)
      how_many_more_ones = [0] * num_bits
    for i in range(num_bits):
      if bits[i] == 1:
        how_many_more_ones[i] += 1
      else:
        how_many_more_ones[i] -= 1

  gamma_bits = [0] * num_bits
  epsilon_bits = [0] * num_bits
  
  for i in range(num_bits):
    if how_many_more_ones[i] >= 0:
      gamma_bits[i] = 1
    elif how_many_more_ones[i] < 0:
      epsilon_bits[i] = 1

  return (gamma_bits, epsilon_bits)


def oxygen_co2(strings):
  current_oxygen_bits_list = list(
    string_to_bits(s) for s in strings)
  current_co2_bits_list = current_oxygen_bits_list
  for i in range(len(current_oxygen_bits_list[0])):
    oxygen_bit = (
      bits_list_to_gamma_epsilon_bits(
        current_oxygen_bits_list)[0][i])
    current_oxygen_bits_list = list(
      b for b in current_oxygen_bits_list if (
        b[i] == oxygen_bit))
    if len(current_co2_bits_list) > 1:
      co2_bit = (
        bits_list_to_gamma_epsilon_bits(
          current_co2_bits_list)[1][i])
      current_co2_bits_list = list(
        b for b in current_co2_bits_list if (
          b[i] == co2_bit))
  if len(current_oxygen_bits_list) != 1:
    raise ValueError(
      'Wrong number of oxygen bits: '
      + str(len(current_oxygen_bits_list)))
  if len(current_co2_bits_list) != 1:
    raise ValueError(
      'Wrong number of co2 bits: '
      + str(len(current_co2_bits_list)))

  return (
    bits_to_int(current_oxygen_bits_list[0]),
    bits_to_int(current_co2_bits_list[0]))

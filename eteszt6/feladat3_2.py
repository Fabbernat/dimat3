def multiplicative_order(element, powers):
  """Meghatározza egy elem multiplikatív rendjét a GF(16) testben."""
  for i, power in enumerate(powers):
    if power == element:
      return i + 1
  return None

powers = [
    [1],
    [1, 1],
    [1, 0, 1],
    [1, 1, 1, 1],
    [0, 1],
    [1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 1, 0],
    [1, 1, 0, 0],
    [1, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 0],
    [1],
]

element1 = [0, 0, 1]
element2 = [1, 1, 0, 0]
element3 = [1, 0, 1, 1]

print(f"Első állítás: {multiplicative_order(element1, powers) == 4}")
print(f"Második állítás: {multiplicative_order(element2, powers) == 5}")
print(f"Harmadik állítás: {multiplicative_order(element3, powers) == 15}")
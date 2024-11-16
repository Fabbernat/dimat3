def multiplicative_order(element, powers):
  """
  Meghatározza egy elem multiplikatív rendjét a GF(16) testben.

  Args:
    element: A GF(16) testbeli elem, polinomként reprezentálva.
    powers: A primitív elem hatványainak listája.

  Returns:
    Az elem multiplikatív rendje, vagy None, ha az elem nem szerepel a listában.
  """
  for i, power in enumerate(powers):
    if power == element:
      return i + 1  # A lista 0-tól indexelt, a rend 1-től
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

# A solver meghívása
print(f"Első állítás: {multiplicative_order(element1, powers) == 15}")
print(f"Második állítás: {multiplicative_order(element2, powers) == 15}")
print(f"Harmadik állítás: {multiplicative_order(element3, powers) == 15}")
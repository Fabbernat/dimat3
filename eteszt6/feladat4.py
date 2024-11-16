from sympy import isprime, GF


def is_field(p, n):
  if not isprime(p):
    return False
  if n <= 0:
    return False
  return True

def is_basis(v1, v2, field):
  if not isinstance(v1, field) or not isinstance(v2, field):
    return False
  if v1 == 0 or v2 == 0:
    return False
  try:
    ratio = v1 / v2
  except ZeroDivisionError:
    return True
  return not isinstance(ratio, field)

def is_primitive_element(element, field, irreducible_poly):
  field_size = len(field)
  powers = {element**i for i in range(field_size)}
  return len(powers) == field_size - 1 and irreducible_poly in powers


# Első állítás
# print(is_field(float, 1))

# Második állítás
print(is_basis(1, 2**0.5, float))

x = 1
# Harmadik állítás
# Z3[x]/(x^2 + 2x + 2) test elemeinek generálása
field_elements = [a*x + b for a in range(3) for b in range(3)]
irreducible_poly = x**2 + 2*x + 2
print(is_primitive_element(x + 1, field_elements, irreducible_poly))


def is_prime_field_isomorphic(field, prime_field):
  """Ellenőrzi, hogy egy test prímteste izomorf-e egy adott prímtesttel."""
  try:
    GF_field = GF(len(field))  # Létrehozza a testet a sympy segítségével
    return GF_field.characteristic == prime_field.characteristic
  except ValueError:
    return False  # Ha a field nem test, akkor False

def count_primitive_elements(field):
  """Megszámolja a primitív elemeket egy véges testben."""
  try:
    GF_field = GF(len(field))
    return len([element for element in GF_field if element.is_primitive_root()])
  except ValueError:
    return None  # Ha a field nem test, akkor None

def is_vector_space(field, base_field, dimension):
  """Ellenőrzi, hogy egy halmaz vektortér-e egy adott test felett."""
  # Egyszerűsített ellenőrzés, feltételezve, hogy a field a base_field feletti polinomok halmaza
  if not isprime(base_field.characteristic):
    return False
  try:
    GF_field = GF(len(field))
    return GF_field.characteristic == base_field.characteristic and GF_field.degree == dimension
  except ValueError:
    return False  # Ha a field nem test, akkor False

# Első állítás
# field1 = GF(2**4, modulus=x**4 + x + 1)  # Z2[x]/(x^4 + x + 1)
prime_field1 = GF(2)  # Z2
# print(f"Első állítás: {is_prime_field_isomorphic(field1, prime_field1)}")

# Második állítás
field2 = GF(3**2)  # GF(9)
print(f"Második állítás: {count_primitive_elements(field2) == 5}")

# Harmadik állítás
field3 = GF(3**2, modulus=2*x**2 + 2)  # Z3[x]/(2x^2 + 2)
base_field3 = GF(3)  # Z3
print(f"Harmadik állítás: {is_vector_space(field3, base_field3, 2)}")
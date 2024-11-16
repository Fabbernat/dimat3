def add_polys(f, g):
  """Összead két polinomot modulo 3."""
  max_len = max(len(f), len(g))
  f = f + [0] * (max_len - len(f))
  g = g + [0] * (max_len - len(g))
  return [(a + b) % 3 for a, b in zip(f, g)]

def mul_polys(f, g):
  """Megszoroz két polinomot modulo 3 és modulo (x^3 + 2x^2 + 1)."""
  result = [0] * (len(f) + len(g) - 1)
  for i, a in enumerate(f):
    for j, b in enumerate(g):
      result[i + j] = (result[i + j] + a * b) % 3
  return reduce_poly(result)

def reduce_poly(f):
  """Redukálja a polinomot modulo (x^3 + 2x^2 + 1)."""
  divisor = [1, 2, 0, 1]
  while len(f) >= len(divisor):
    factor = f[-1] / divisor[-1]
    for i in range(len(divisor)):
      f[-i - 1] = (f[-i - 1] - factor * divisor[-i - 1]) % 3
    f = f[:-1]
  return [int(coeff) for coeff in f]

def inverse_poly(f):
  """Meghatározza a polinom inverzét modulo (x^3 + 2x^2 + 1)."""
  a, b = f, [1, 2, 0, 1]
  u, v = [1], [0]
  while b != [0]:
    q, r = divmod_polys(a, b)
    a, b = b, r
    u, v = v, add_polys(u, mul_polys(q, v))
  if a == [1]:  # Ha a maradék 1, akkor van inverz
    return reduce_poly(u)
  else:
    return None  # Ha a maradék nem 1, akkor nincs inverz

def divmod_polys(f, g):
  """Eloszt két polinomot."""
  if len(g) == 1:  # Ha g konstans
    return [int(coeff / g[0]) % 3 for coeff in f], [0]
  q = [0] * (len(f) - len(g) + 1)
  r = f[:]
  while len(r) >= len(g) and r != [0]:
    factor = r[-1] / g[-1]
    q[len(r) - len(g)] = factor
    for i in range(len(g)):
      r[-i - 1] = (r[-i - 1] - factor * g[-i - 1]) % 3
    r = r[:-1]
  return [int(coeff) for coeff in q], [int(coeff) for coeff in r]

def check_equality(f, g, h):
  """Ellenőrzi, hogy f^-1 * g = h egyenlőség teljesül-e GF(27)-ben."""
  f_inv = inverse_poly(f)
  if f_inv is None:
    return False  # Ha f-nek nincs inverze, akkor az egyenlőség hamis
  left_side = reduce_poly(mul_polys(f_inv, g))
  return left_side == h

# A feladatban szereplő polinomok
f1 = [2, 1]  # 2x + 1
g1 = [2, 0, 2]  # 2x^2 + 2
h1 = [2, 0, 0]  # 2x^2

f2 = [2, 2]  # 2x + 2
g2 = [1, 0, 1]  # x^2 + 1
h2 = [1, 0, 2]  # x^2 + 2

f3 = [1, 2]  # x + 2
g3 = [1, 0, 1]  # x^2 + 1
h3 = [1, 1]  # x + 1

# Az egyenlőségek ellenőrzése
print(f"Első egyenlőség: {check_equality(f1, g1, h1)}")
print(f"Második egyenlőség: {check_equality(f2, g2, h2)}")
print(f"Harmadik egyenlőség: {check_equality(f3, g3, h3)}")
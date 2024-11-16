from itertools import product


def gpt_is_irreducible(f): # helyesen dönti el a polinomok irreducibilitását ℤ<sub>3</sub> felett
    """
    Eldönti, hogy egy f polinom irreducibilis-e Z3 felett.

    Args:
      f: A polinom együtthatóinak listája, a legmagasabb fokú tagtól kezdve.
         Például x^2 + 2x + 2 esetén a lista [1, 2, 2].

    Returns:
      True, ha f irreducibilis Z3 felett, False egyébként.
    """
    def eval_poly(f, x):
        """Kiértékeli a polinomot egy adott x értéknél."""
        result = 0
        for i, coeff in enumerate(f[::-1]):
            result += coeff * x**i
        return result % 3

    def poly_mult(p1, p2):
        """Két polinom szorzata Z3 felett."""
        deg = len(p1) + len(p2) - 2
        result = [0] * (deg + 1)
        for i, a in enumerate(p1):
            for j, b in enumerate(p2):
                result[i + j] = (result[i + j] + a * b) % 3
        return result

    # Ellenőrizzük a gyököket
    for x in range(3):
        if eval_poly(f, x) == 0:
            return False

    degree = len(f) - 1

    # Másodfokú vagy harmadfokú polinomok
    if degree in [2, 3]:
        return True

    # Negyedfokú polinomok
    if degree == 4:
        # Próbáljuk felbontani két másodfokú polinom szorzatára
        for a, b, c in product(range(3), repeat=3):
            if a == 0:
                continue
            g = [a, b, c]  # Másodfokú polinom
            quotient, remainder = divmod_poly(f, g)
            if len(remainder) == 0 and len(quotient) == 3:
                return False
    return True

def divmod_poly(f, g):
    """Osztás polinomokkal Z3 felett."""
    f = f[:]
    quotient = []
    while len(f) >= len(g):
        lead_coeff = f[0] * pow(g[0], 2, 3) % 3
        quotient.append(lead_coeff)
        for i in range(len(g)):
            f[i] = (f[i] - lead_coeff * g[i]) % 3
        f.pop(0)
    return quotient, f

"""
A polynomials tömbbe csak az együtthatókat kell beleírni, kezdve a legnagyobb fokszámúval a konstansig
példa használatra:
f1 = 2*x**3 (+ 0*x**2) + 2*x + 1
f2 = x**2 + x + 2
f3 = x**3 (+ 0*x**2) + 2*x + 1

polynomials = [
    [2, 0, 2, 1],
    [1, 1, 2],
    [1, 0, 2, 2]
]
"""

polynomials = [
    [2, 2, 1],
    [1, 1, 0, 2],
    [1, 1, 2, 1]
]

# Eredmény kiszámítása mindhárom polinomra
results = [gpt_is_irreducible(poly) for poly in polynomials]
for i in range(len(results)):
    print(f"{i + 1}. feladat megoldása: {results[i]}")
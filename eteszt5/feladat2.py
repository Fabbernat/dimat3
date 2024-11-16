from sympy import Poly, GF
from sympy.abc import x


def is_polynomial_irreducible(poly_expr, domain):
    """
    Meghatározza, hogy egy polinom irreducibilis-e egy adott gyűrű felett.

    :param poly_expr: A polinom kifejezése.
    :param domain: A polinom gyűrűje (pl. 'C' komplex számok, GF(2) véges test).
    :return: True, ha a polinom irreducibilis, False egyébként.
    """

    # Polinom létrehozása a megadott kifejezésből és gyűrűből
    poly = Poly(poly_expr, x, domain=domain)

    # Irreducibilitás vizsgálata
    if domain == 'C':
        # Ideiglenes megoldás: False, amíg nem találunk jobb módszert
        # A komplex számok esetén keressünk más irreducibilitás tesztet!
        return False
    else:
        return poly.is_irreducible


# Példa a feladatban található adatok ellenőrzésére
# Az egyes válaszok polinomjai és a hozzájuk tartozó gyűrű
answers_example = [
    (27 * x ** 2 + 10 * x, 'C'),  # komplex számok gyűrűje C[x]
    (x - 1, 'C'),  # komplex számok gyűrűje C[x]
    (x ** 3 + x ** 2 + x + 1, GF(2))  # véges test Z2[x]
]

answers = [
    (2 * x ** 2 + x, GF(3)),
    (x ** 3 + x + 1, GF(2)),
    (x ** 3 + x ** 2 + 1, GF(2))
]


polynomials = [
    (2 * x**2 + x, GF(3)),
    (x**3 + x + 1, GF(2)),
    (x**3 + x**2 + 1, GF(2))
]

# Az eredmények kiíratása
for i, (poly_expr, domain) in enumerate(polynomials, 1):
    is_irreducible = is_polynomial_irreducible(poly_expr, domain)
    print(f"{i}. válasz irreducibilitása: {'Irreducibilis' if is_irreducible else 'Nem irreducibilis'}")

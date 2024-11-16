from typing import List


# GF(27)-beli maradékosztás (x^3 + 2x^2 + 1 polinommal)
def mod_poly(p: List[int]) -> List[int]:
    """Az x^3 + 2x^2 + 1 modulis osztás eredményét adja vissza."""
    # Modulálás alapja: x^3 + 2x^2 + 1
    modulus = [1, 2, 0, 1]  # 1*x^3 + 2*x^2 + 0*x + 1
    while len(p) > 3:
        # Leading term reduction
        factor = p[0]  # vezető együttható
        for i in range(4):  # modulus polinom fokszáma
            p[i] = (p[i] - factor * modulus[i]) % 3
        p.pop(0)  # csökkentjük a fokot
    return p


# Polinom összeg
def add_poly(p1: List[int], p2: List[int]) -> List[int]:
    """Polinomok összeadása Z3 felett."""
    length = max(len(p1), len(p2))
    p1 = [0] * (length - len(p1)) + p1
    p2 = [0] * (length - len(p2)) + p2
    return [(p1[i] + p2[i]) % 3 for i in range(length)]


# Polinom szorzás
def multiply_poly(p1: List[int], p2: List[int]) -> List[int]:
    """Polinomok szorzása Z3 felett, mod x^3 + 2x^2 + 1."""
    result = [0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] = (result[i + j] + p1[i] * p2[j]) % 3
    return mod_poly(result)


# A három állítás vizsgálata
def check_statement(statement_number: int) -> bool:
    if statement_number == 1:
        left = add_poly([0, 2, 1], multiply_poly([2, 0, 1], [2]))  # 2x + 1 + 2x^2 * 2
        right = [0, 2, 2]  # 2x^2
    elif statement_number == 2:
        left = add_poly([2, 0, 1], multiply_poly([2], [0, 1, 1]))  # 2x + 2 * x^2 + 1
        right = add_poly([1, 0, 1], [0, 2])  # x^2 + 2x
    elif statement_number == 3:
        left = add_poly([1, 0, 1], multiply_poly([2], [0, 1, 1]))  # x + 2 * x^2 + 1
        right = [1, 1]  # x + 1
    else:
        raise ValueError("Érvénytelen állítás sorszám")

    # Ellenőrizzük, hogy bal oldal = jobb oldal
    return left == right


# Példa a három állítás ellenőrzésére
print(f"Az első állítás igaz: {check_statement(1)}")
print(f"A második állítás igaz: {check_statement(2)}")
print(f"A harmadik állítás igaz: {check_statement(3)}")

from sympy import symbols, GF, Poly, div


def check_equation(poly_left_coeffs, poly_right_coeffs, modulus_coeffs, p):
    """Ellenőrzi, hogy a bal és jobb oldal egyenlő-e adott modulus és modulo p mellett."""
    x = symbols('x')
    modulus = Poly(modulus_coeffs, x, domain=GF(p))

    # Bal és jobb oldal definiálása
    poly_left = Poly(poly_left_coeffs, x, domain=GF(p))
    poly_right = Poly(poly_right_coeffs, x, domain=GF(p))

    # Bal oldal modulus alapján
    _, remainder_left = div(poly_left, modulus)
    _, remainder_right = div(poly_right, modulus)

    return remainder_left == remainder_right


# Egyenletek koefficiensei a bal és jobb oldalra
equations = [
    ([2, 1, 0, 2, 2], [0, 2, 0]),  # 2x + 1 * 2x^2 + 2 = 2x^2
    ([2, 1, 1, 0, 1], [1, 0, 2]),  # 2x + 1 * x^2 + x = x^2 + 2
    ([2, 2, 1, 2, 1], [0, 2, 0])  # 2x + 2 * x^2 + 2x + 1 = 2x^2
]

# Modulust jelentő polinom koefficiensei
modulus_coeffs = [1, 2, 0, 1]

# Eredmények kiszámítása mindhárom egyenletre
results = [check_equation(eq[0], eq[1], modulus_coeffs, 3) for eq in equations]

# Kimenet eredményekkel
print(results)

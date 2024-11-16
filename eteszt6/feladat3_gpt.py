from typing import List

# Moduláris polinom T = Z2[x]/<x^4 + x + 1>
MODULUS = [1, 0, 0, 0, 1, 1]  # x^4 + x + 1

def mod_poly(p: List[int], modulus: List[int]) -> List[int]:
    """Osztja a p polinomot a modulus polinommal Z2 felett, visszaadva a maradékot."""
    p = p[:]
    while len(p) >= len(modulus):
        if p[0] == 1:  # Csak akkor vonjuk ki, ha a vezető együttható 1
            for i in range(len(modulus)):
                p[i] = (p[i] + modulus[i]) % 2
        p.pop(0)  # Csökkentjük a fokot
    return p

def multiply_poly(p1: List[int], p2: List[int], modulus: List[int]) -> List[int]:
    """Polinomok szorzása Z2 felett, modulus polinommal."""
    result = [0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] = (result[i + j] + p1[i] * p2[j]) % 2
    return mod_poly(result, modulus)

def poly_pow(base: List[int], exp: int, modulus: List[int]) -> List[int]:
    """Hatványozza a polinomot a Z2[x] modulo modulus testben."""
    result = [1]  # egységelem (1)
    power = base
    while exp > 0:
        if exp % 2 == 1:
            result = multiply_poly(result, power, modulus)
        power = multiply_poly(power, power, modulus)
        exp //= 2
    return result

def check_multiplicative_order_15(poly: List[int]) -> bool:
    """Ellenőrzi, hogy a megadott polinomnak 15-ös multiplikatív rendje van-e."""
    # Számítsuk ki a 15. hatványát, és nézzük meg, hogy 1-e az eredmény
    return poly_pow(poly, 15, MODULUS) == [1]

# Polinomok listázása a kérdések alapján
polynomials = [
    [0, 0, 0, 1],      # x^3
    [0, 0, 1, 1],      # x^3 + x^2
    [0, 1, 0, 1]       # x^3 + x + 1
]

# Ellenőrzés
for i, poly in enumerate(polynomials, start=1):
    result = check_multiplicative_order_15(poly)
    print(f"A(z) {i}. polinom multiplikatív rendje 15: {result}")

from sympy import symbols, Poly, GF, gcd

# A polinom változó definiálása
x = symbols('x')


def check_lnko(f_expr, g_expr, given_lnko_expr):
    """
    Ellenőrzi, hogy a két megadott polinom legnagyobb közös osztója megegyezik-e
    a megadott értékkel a Z2[x] gyűrűben.

    :param f_expr: Az első polinom kifejezése (például x**4 + x**2 + 1).
    :param g_expr: A második polinom kifejezése (például x**4 + x**3 + x**2).
    :param given_lnko_expr: A megadott legnagyobb közös osztó kifejezése (például x**2 + 1).
    :return: True, ha helyes a megadott legnagyobb közös osztó, különben False.
    """
    # Polinomok létrehozása a Z2 test felett
    f = Poly(f_expr, x, domain=GF(2))
    g = Poly(g_expr, x, domain=GF(2))
    given_lnko = Poly(given_lnko_expr, x, domain=GF(2))

    # Legnagyobb közös osztó kiszámítása
    actual_lnko = gcd(f, g)

    # Ellenőrzés
    return actual_lnko == given_lnko


# Példa a feladatban található adatok ellenőrzésére
# Az egyes válaszok alapján megadott polinomok és a feltételezett lnko értékek
answers_example = [
    (x ** 4 + x ** 2 + 1, x ** 4 + x ** 3 + x ** 2, x ** 2 + 1),
    (x ** 4 + x ** 3, x ** 4 + x ** 3 + x, 1),
    (x ** 4 + x ** 3 + x ** 2 + 1, x ** 4 + x ** 3 + x + 1, x + 1)
]

answers = [
    (x ** 4 + x ** 3 + x + 1, x ** 4 + x ** 3 + x ** 2, x ** 2 + 1),
    (x ** 4 + x ** 3, x ** 4 + x ** 3 + x, x),
    (x ** 4 + x ** 3 + x + 1, x ** 4 + x + 1,  1)
]

# Az eredmények kiíratása
for i, (f_expr, g_expr, given_lnko_expr) in enumerate(answers, 1):
    is_correct = check_lnko(f_expr, g_expr, given_lnko_expr)
    print(f"{i}. válasz helyessége: {'Helyes' if is_correct else 'Helytelen'}")

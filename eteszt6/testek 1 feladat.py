from sympy import Poly, GF
from sympy.abc import x

print("Írd be f értékének a képletet. A hatványt írd simán az x mögé.\n")
'''pl: 
f = x3+2x2+x+2
'''

f = "x3+x2+2x+1"


def polizalo(exp):
    k = ''
    for i, c in enumerate(exp):
        if c in "123456789":
            if 0 < i < len(exp)-1:
                if exp[i + 1]== 'x':
                    k+=c+'*'

                if exp[i - 1]== 'x':
                    k+='**'+c
            else:
                if i==0 and len(exp)>1:
                    if exp[i + 1]== 'x':
                        k+=c+'*'
                    else:
                        k+=c
                if i==len(exp)-1and len(exp)>1:
                    if exp[i - 1]== 'x':
                        k+='**'+c
                    else:
                        k+=c
                if len(exp)==1:
                    k += c
        else:
            k += c
    #print(k)
    return k


def is_polynomial_irreducible(poly_expr, domain=GF(3)):

    poly = Poly(poly_expr, x, domain=domain)

    return poly.is_irreducible

f=polizalo(f)
print(f)

exec(f"f = {f}")

print(f"{'Igaz' if is_polynomial_irreducible(f) else 'Hamis'}")

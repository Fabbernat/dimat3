from sympy import Poly, GF
from sympy.abc import x

print("Írd be f1, f2 és equals értékének a képletet. A hatványt írd simán az x mögé.\n"
      "HA A BAL KÉPLET -1 RE VAN EMELVE f2 ÉRTÉKÉNEK ÍRJ -1 ET.\n")
'''pl:
f1 = "2x2+2x+2"
f2 = "-1"
equals = "2x2+x+1"
'''

f1 = "2x+2"
f2 = "x2+1"
equals = "x2+2x"


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


def feladat(f1, f2, equals, domain=GF(3)):

    f1 = Poly(f1, x, domain=domain)
    equals = Poly(equals, x, domain=domain)
    z = x ** 3 + 2 * x ** 2 + 1
    z = Poly(z, x, domain=domain)

    if f2 != -1 and f2 != '-1':
        f2 = Poly(f2, x, domain=domain)

        res = f1*f2
        #print(res)

        res %= z
        #print(res)
        return res == equals
    else:
        res = f1 * equals
        #print(res)
        res %= z
        #print(res)
        return res == 1


f1=polizalo(f1)
equals=polizalo(equals)

if f2 != -1 and f2 != '-1':
    f2 = polizalo(f2)
    print(f"({f1}) * ({f2}) = {equals}")
else:
    print(f"({f1})**({f2}) = {equals}")


exec(f"f1 = {f1}")
exec(f"f2 = {f2}")
exec(f"equals = {equals}")

print(f"{'Igaz' if feladat(f1, f2, equals) else 'Hamis'}")


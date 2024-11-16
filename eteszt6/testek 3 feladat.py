from sympy import Poly, GF
from sympy.abc import x

print("Írd be f1, és equals értékének a képletet. A hatványt írd simán az x mögé.\n"
      "Ha minimálpolinomot kér a feladat_tipusnak 0 át írj. Ha multiplikatív rendjét akkor 1 et írj.\n")
'''pl:
feladat_tipus = 1
f1 = "x3+1"
equals = "15"
'''

feladat_tipus = 0  # minimal = 0, multi = 1
f1 = "x2+1"
equals = "x4+x+1"


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


def minimalpolinom(f, domain=GF(2)):
        f = Poly(f, x, domain=domain)
        z = x ** 4 + x + 1
        z = Poly(z, x, domain=domain)
        res = f%z
        #print(res)
        return res==0


def multiplikativ(f, mult, domain=GF(2)):
    if mult == 0:
        return True

    f = Poly(f, x, domain=domain)
    z = x ** 4 + x + 1
    z = Poly(z, x, domain=domain)
    f%=z

    res = f
    for k in range(mult-1):
        if res == 1 and k != mult-2:
            return False
        res*=f
        res%=z

    #print(res)
    return res == 1


f1=polizalo(f1)
equals=polizalo(equals)

if not feladat_tipus:
    f=equals.replace('x', f'({f1})')
    #print(f)
    exec(f"f = {f}")
    #print(f)
    print(f"{f1} minimálpolinomja {equals}")
    print(f"{'Igaz' if minimalpolinom(f) else 'Hamis'}")
else:
    f = f1
    exec(f"f = {f}")
    #print(f)
    print(f"{f1} multiplikatív rendje {equals}")
    print(f"{'Igaz' if multiplikativ(f, int(equals)) else 'Hamis'}")




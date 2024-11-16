import numpy as np

a = [[1, 0],
     [0, 0]]

b = [[1, 2],
     [3, 4]]

r = [[0, 1],
     [-1, 0]]


a = np.array(a)
b = np.array(b)
r = np.array(r)


print("Mátrixok: a, b, r")
egyenlet = input("Írd be az egyenletet. Ezen karakterekből, space nélkül: a b r + - 0123456789\n Hatványozás nincs, töbször kell beirni egymás után a mátrix jelét.\n")
teszt= True
while teszt:
    teszt = False
    for k in egyenlet:
        if k not in "abr+-*^()0123456789":
            print("helytelen egyenlet, probáld újra")
            teszt = True
            egyenlet = input()
            break

#print(egyenlet, '\n')

egym = ""
for k, v in enumerate(egyenlet):
    if k + 1 < len(egyenlet) and egyenlet[k + 1] not in "-+" and v not in "-+":
        egym += v+"*"
    else:
        egym += v

print(egym, '\n')

fix = ""
for k, v in enumerate(egym):
    if v != "*":
        fix += v
    else:
        if egym[k-1] in "abr" and egym[k+1] in "abr":
            fix += "@"
        else:
            fix += "*"

res = None

exec(f"res = {fix}")

print("fi = \n", res, '\n')
print("ha egyezik pipa")



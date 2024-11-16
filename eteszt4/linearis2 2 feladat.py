import numpy as np
print('Írd be a mátrixot és a vektort a skript első soraiba.')

# ide írd

A = [[-2, -4],
     [2, -1]]

v = (2, 1)


A = np.array(A)
v = np.array(v)

res = v @ A
oszto = res[0] / v[0]
print(res)
print('λ=', oszto)
print()

megoldas = v[0]*oszto == res[0] and v[1]*oszto == res[1]

print('Az állitás:', 'Igaz' if megoldas else 'Hamis')

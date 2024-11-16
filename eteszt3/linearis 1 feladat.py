import numpy as np
from scipy.linalg import lu
print("írd be a szkript első soraiba a változokat.\n")

# ide ird
v1 = [-2, 2]
v2 = [0, 2]

A = [[-2, -2],
     [-1, 0]]

# fi jel elötti 2 szám
fi = [0, -2]


v1 = np.array(v1)
v2 = np.array(v2)
A = np.array(A)
fi = np.array(fi)

u = np.array([v1[0], v2[0], fi[0]])
l = np.array([v1[1],  v2[1], fi[1]])

arr = np.array([u, l])
_, ga = lu(arr, permute_l=True)
#print(ga)

ga[1] /= ga[1][1]
#print(ga)

ga[0] -= ga[0][1]*ga[1]
#print(ga)

ga[0] /= ga[0][0]
#print(ga)
#print()

a = ga[0][2]
b = ga[1][2]

#print(a, b)

mult = np.array([a, b]) @ A
#print(mult)

result = mult[0] * v1 + mult[1] * v2

print(fi, "fi =", result, "\n")
print("ha egyezik pipa")

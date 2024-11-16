# meg 33 pont kell otoshoz.

import numpy as np

# A mátrix definiálása
A = np.array([[-2, 2, 0],
              [2, 1, 0],
              [1, 2, 0]])

# A sajátértékek és sajátvektorok meghatározása
eigenvalues, eigenvectors = np.linalg.eig(A)

# Kiválasztjuk azokat a sajátvektorokat, amelyekhez a sajátérték 0
eigenvectors_zero = eigenvectors[:, np.isclose(eigenvalues, 0)]

# Az eredmény kiírása
print("λ = 0 sajátértékhez tartozó sajátvektor(ok):")
print(eigenvectors_zero)

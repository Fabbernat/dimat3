"""
7. hét
Sziasztok!

A 7. héten a következő feladatokkal foglalkoztunk:

3.1ad, 3.2c, 3.3b, 3.4a, 3.5a, 3.6a, 3.7f (itt csak az egyik sajátértékhez adtuk meg a sajátalteret).

A következő héten ezekhez hasonló feladatok lehetnek a röpdolgozatban.



Ezen a gyakorlaton gyorsabban kellett haladnunk; lényegében megcsináltuk a 3. feladatsor feladatait. Mivel a legtöbb feladattípusra csak 1 példát néztünk, érdemes otthon gyakorolni, esetleg megnézni ezekhez a feladattípusokhoz a videókat.

Persze ha valakinek szüksége van rá, van lehetőség hozzám is fordulni segítségért, csak időpontot kell egyeztetni. Akkor is írjatok, ha meg szeretnétek nézni az 1. ZH-t, mert a következő gyakorlatra már nem fogom bevinni.
"""

import numpy as np
from scipy import linalg

def determine_linear_transformation(matrix):
    """
    Determines the kernel, image, dimensions, and bases of a linear transformation given its matrix.

    Args:
        matrix: A numpy array representing the linear transformation matrix.

    Returns:
        A tuple containing the kernel, image, dimensions, and bases.
    """

    # Find the kernel (null space)
    kernel = np.null_space(matrix)

    # Find the image (column space)
    image = matrix.T  # Transpose to find row space, which is the same as the column space
    image = np.null_space(image).T  # Find the orthogonal complement of the row space

    # Calculate dimensions
    dim_kernel = kernel.shape[1]
    dim_image = image.shape[1]

    # Return the results
    return kernel, image, dim_kernel, dim_image

# Example usage
# Assuming a matrix A is given (replace with the actual matrix)
A = np.array([[1, 2], [3, 4]])

kernel, image, dim_kernel, dim_image = determine_linear_transformation(A)

print("Kernel:")
print(kernel)
print("Image:")
print(image)
print("Dimension of kernel:", dim_kernel)
print("Dimension of image:", dim_image)
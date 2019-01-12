import numpy as np
import math

x = np.array([3, 4])


# Huong cua vector
def direction(x):
    return x / np.linalg.norm(x)


# Tich vo huong
def geometric_dot_product(x, y, theta):
    x_norm = np.linalg.norm(x)
    y_norm = np.linalg.norm(y)
    return x_norm * y_norm * math.cos(math.radians(theta))


# Tich vo huong n chieu
def dot_product(x, y):
    result = 0
    for i in range(len(x)):
        result = result + x[i] * y[i]
    return result


print(np.linalg.norm(x))
print(direction([3, 4]))
print(geometric_dot_product([3, 5], [8, 2], 45))
print(dot_product([3, 5], [8, 2]))
print(np.dot([3, 5], [8, 2]))

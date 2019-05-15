import numpy as np
from numba import jit

d_a = np.genfromtxt('08.txt', delimiter=1)  # digits array
d_a = d_a.reshape(d_a.shape[0] * d_a.shape[1])


def substrings(n, x):
    return np.fromfunction(lambda i, j: x[i + j], (len(x) - n + 1, n), dtype=int)


a = substrings(13, d_a)

a_multiply = np.prod(a, axis=1)

ind = np.where(a_multiply == np.max(a_multiply))

print(a[ind])
print(np.max(a_multiply))

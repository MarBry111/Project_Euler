import numpy as np 
from numba import jit

d_a = np.genfromtxt('08.txt', delimiter = 1) #digits array
d_a = d_a.reshape(1,d_a.shape[0]*d_a.shape[1])
print(d_a.shape)

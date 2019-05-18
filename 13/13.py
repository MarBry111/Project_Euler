import numpy as np

d_a = np.genfromtxt('13.txt', delimiter='\n')  # digits array

print(np.sum(d_a))

import numpy as np
from numba import jit

d_a = np.genfromtxt('11.txt', delimiter=" ")  # digits array

#What is the greatest product of four adjacent numbers in the same 
#direction (up, down, left, right, or diagonally) in the 20×20 grid?

def substrings(n, x):
    return np.fromfunction(lambda i, j: x[i + j], (len(x) - n + 1, n), dtype=int)

def substrings_diagonal(n,arr):
	diag_arr = []
	for i in range(arr.shape[0]-n):
		temp_arr = []
		for j in range(n):
			temp_arr.append(arr[i+j,j])
		diag_arr.append(temp_arr)
	for i in range(arr.shape[0]-n):
		i=i+4
		temp_arr = []
		for j in range(n):
			temp_arr.append(arr[i-j,j])
		diag_arr.append(temp_arr)
	return(np.array(diag_arr))

def look_for_max(arr = None):
	max_all = 0
	for i in range(arr.shape[0]):
		max_row = np.max(np.prod(substrings(4,arr[i,:]), axis=1))
		if max_row>max_all: 
			max_all=max_row
	for i in range(arr.shape[1]):
		max_col = np.max(np.prod(substrings(4,arr[:,i]), axis=1))
		if max_col>max_all: 
			max_all=max_col
	for i in range(arr.shape[0]-4):
		#print(np.prod(substrings_diagonal(4,arr[:,i:]), axis=1).shape)
		max_diag = np.max(np.prod(substrings_diagonal(4,arr[:,i:]), axis=1))
		if max_diag>max_all: 
			max_all=max_diag
	print(max_all)

look_for_max(d_a)
from numba import jit
import numpy as np

@jit
def check_prime(n):
	#if n is even then not prime
	if n%2==0: return False
	#we only check to the ceil(sqrt(n)) +1 if it divide
	iterator = np.arange(3,np.ceil(np.sqrt(n))+1,2)
	for i in iterator:
		#if there is no rest after dividing then n is not a even
		if n%i==0: return False
	#if program ended here then n is odd
	return True

#add 2 as first prime
suma = 2
#primes = [2]
n= 2000000
check = np.arange(3,n,2)
for j in check:
	if check_prime(j): 
		#primes.append(j)
		suma = suma+j

print(suma)
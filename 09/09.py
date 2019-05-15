from math import sqrt

def look():
	for i in range(1, 500):
		for j in range(1, 1000):
			c=sqrt(i**2+j**2)
			if (c).is_integer() and i+j+c ==1000 and i!=j:
				print(i,j,c)
				print(i*j*c)
				return(i*j*c)

look()
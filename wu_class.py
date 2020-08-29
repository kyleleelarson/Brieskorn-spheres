# function that takes a list representing a linear plumbing
# with the first two elements marked (0 not in, 1 in) and returns a list
# representing the spherical wu class, or empty list if does not exist

import numpy as np

def wu(l: list, w0: int, w1: int):
	w = np.zeros((len(l),), dtype=int) #list representing wu class
	w[0] = w0
	w[1] = w1
	for i in range(1,len(l)-1):
		if l[i] % 2 == 1:
			if w[i] == 0 and w[i-1] == 0:
				w[i+1] = 1
		else:
			if w[i-1] == 1:
				w[i+1] = 1
	# consider viability of last entry of list
	if l[-1] % 2 == 1:
		if w[-1] == 1 or w[-2] == 1:
			return w
	if l[-1] % 2 == 0:
		if w[-1] == 1 or w[-2] == 0:
			return w
	# else return []
	return []
	

#print(wu([2,3,3,2,5,2],0,1))
# function that takes Seifert invariants defining a Brieskorn sphere
# and returns the corresponding linking matrix

import numpy as np
from continued_fractions import cont_frac

def plumb_mat(b,a1,b1,a2,b2,a3,b3): # returns the matrix corresponding to the Seifert invariants
	l1 = cont_frac(a1,b1)
	l2 = cont_frac(a2,b2)
	l3 = cont_frac(a3,b3)
	dim = 1 + len(l1) + len(l2) + len(l3)
	A = np.zeros((dim,dim), dtype=int)
	A[0,0] = b
	A[0,1 + len(l1)] = 1
	A[1 + len(l1),0] = 1
	A[0,1 + len(l1) + len(l2)] = 1
	A[1 + len(l1) + len(l2),0] = 1
	for i in range(len(l1)):
		A[1+i,1+i] = l1[i]
		A[1+i,i] = 1
		A[i,1+i] = 1
	for i in range(len(l2)):
		s = 1 + len(l1)
		A[s+i,s+i] = l2[i]
		if i > 0:
			A[s+i,s+i-1] = 1
			A[s+i-1,s+i] = 1
	for i in range(len(l3)):
		s = 1 + len(l1) + len(l2)
		A[s+i,s+i] = l3[i]
		if i > 0:
			A[s+i,s+i-1] = 1
			A[s+i-1,s+i] = 1
	return A
	
#plumb_mat(2,2,1,3,2,5,4)
#(1,2,1,3,1,7,1)
#print(np.linalg.eig(plumb_mat(1,2,1,3,1,5,1))[0])

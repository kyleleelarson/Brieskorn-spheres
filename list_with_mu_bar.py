# create a list of triples defining Brieskorn spheres
# compute mu bar invariant and include as first entry in row
import numpy as np
from continued_fractions import cont_frac
from math import gcd
from wu_class import wu
import matplotlib.pyplot as plt
import seaborn as sns

# function to find the first positive b_i, where x = a_i
# when producing Seifert invariants from a Brieskorn triple
def bi(x,y,z): 
	b = 1
	while True:
		if b*y*z % x == 1:
				return b
		b+=1

f = open('Brieskorn_triples_with_mu_bar.txt','w')
count = 0
mu_list = []
for i0 in range(2, 200):
	for j in range(i0+1,200):
		for k in range(j+1,200):
			if gcd(i0,j) == 1 and gcd(k,j) == 1 and gcd(i0,k) == 1:
				##################################
				# produce Seifert invariants, using first all positive solution
				a1, a2, a3 = i0, j, k
				b1 = bi(a1,a2,a3)
				b2 = bi(a2,a1,a3)
				b3 = bi(a3,a1,a2)
				b = int((b1*a2*a3 + a1*b2*a3 + a1*a2*b3 - 1) / (a1*a2*a3))

				
				# create plumbing matrix
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
				#print(A)			
						
				# find spherical wu class
				w1 = list(wu([b]+l1,1,0))
				w2 = list(wu([b]+l2,1,0))
				w3 = list(wu([b]+l3,1,0))
				if not w1 or not w2 or not w3:
					if b % 2 == 0:
						w1 = list(wu([b]+l1,0,1))
						w2 = list(wu([b]+l2,0,1))
						w3 = list(wu([b]+l3,0,0))	
						if not w1 or not w2 or not w3:
							w1 = list(wu([b]+l1,0,1))
							w2 = list(wu([b]+l2,0,0))
							w3 = list(wu([b]+l3,0,1))
							if not w1 or not w2 or not w3:
								w1 = list(wu([b]+l1,0,0))
								w2 = list(wu([b]+l2,0,1))
								w3 = list(wu([b]+l3,0,1))
								if not w1 or not w2 or not w3:
									w1 = list(wu([b]+l1,0,0))
									w2 = list(wu([b]+l2,0,0))
									w3 = list(wu([b]+l3,0,0))
					else:
						w1 = list(wu([b]+l1,0,1))
						w2 = list(wu([b]+l2,0,1))
						w3 = list(wu([b]+l3,0,1))
						if not w1 or not w2 or not w3:
							w1 = list(wu([b]+l1,0,1))
							w2 = list(wu([b]+l2,0,0))
							w3 = list(wu([b]+l3,0,0))
							if not w1 or not w2 or not w3:
								w1 = list(wu([b]+l1,0,0))
								w2 = list(wu([b]+l2,0,1))
								w3 = list(wu([b]+l3,0,0))
								#if w1 == [] or w2 == [] or w3 == []:
								if not w1 or not w2 or not w3:
									w1 = list(wu([b]+l1,0,0))
									w2 = list(wu([b]+l2,0,0))
									w3 = list(wu([b]+l3,0,1))	
				w = w1 + w2[1:] + w3[1:]
				w = np.asarray(w)
				#print(w)
						
				# calculate mu bar
				sig = 0 # first calculate the signature of A
				eigs = np.linalg.eig(A)[0]
				for e in eigs:
					if e < 0:
						sig-=1
					else: sig+=1
				sq = np.dot(w,np.dot(A,w))
				#print(sq)
				mu = int((sig - sq)/8)
				mu_list.append(mu)
				#print(mu)
				f.write(str(mu)+' '+str(i0)+' '+str(j)+' '+str(k)+'\n')
				count+=1
f.close()
print('Total number = %d' % count)

# to visualize distribution of mu
#ax = sns.distplot(mu_list, kde=False, rug=True)
#plt.show()

zero = 0
for m in mu_list:
	if m == 0:
		zero+=1
print('%d have vanishing mu bar, and %d do not' % (zero, count - zero))

#for indices < 50, get 5231 triples
#for indices < 60, get 9141 triples
#for indices < 70, get 14520 triples
#for indices < 100, get 43519 triples
#for indices < 200, get 372760 triples

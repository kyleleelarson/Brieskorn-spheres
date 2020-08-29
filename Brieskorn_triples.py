# create a list of triples defining Brieskorn spheres

from math import gcd

f = open('Brieskorn_triples.txt','w')
count = 0
for i in range(2, 50):
	for j in range(i+1,50):
		for k in range(j+1,50):
			if gcd(i,j) == 1 and gcd(k,j) == 1 and gcd(i,k) == 1:
				f.write(str(i)+' '+str(j)+' '+str(k)+'\n')
				count+=1
f.close()
print('Total number = %d' % count)

#for indices < 50, get 5231 triples
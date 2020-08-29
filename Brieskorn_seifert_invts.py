# produce Seifert invariants from a Brieskorn triple, write to file

def bi(x,y,z): #function to find the first positive b_i, where x = a_i
	b = 1
	while True:
		if b*y*z % x == 1:
				return b
		b+=1


f = open('Brieskorn_triples_with_mu_bar.txt','r')
fout = open('Brieskorn_invts_plus_mu.txt', 'w')
for l in f:
	l = l[:-1] #strip off \n
	l = l.split() #convert to list
	mu = int(l[0])
	a1, a2, a3 = int(l[1]), int(l[2]), int(l[3])
	b1 = bi(a1,a2,a3)
	b2 = bi(a2,a1,a3)
	b3 = bi(a3,a1,a2)
	# generate other invariants, by adding +/- ai to bi 
	for i in [1,2]: 
		b1 = b1 + (-1)**i * a1
		for j in [1,2]:
			b2 = b2 + (-1)**j * a2
			for k in [1,2]:
				b3 = b3 + (-1)**k * a3
				b = int((b1*a2*a3 + a1*b2*a3 + a1*a2*b3 - 1) / (a1*a2*a3))
				#print("(b;a1/b1,a2/b2,a3/b3) = (%d;%d/%d,%d/%d,%d/%d)" % (b,a1,b1,a2,b2,a3,b3))
				fout.write(str(mu)+' '+str(b)+' '+str(a1)+' '+str(b1)+' '+str(a2)+' '+str(b2)+' '+str(a3)+' '+str(b3)+'\n')

f.close()
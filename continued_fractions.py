# calculate continued fractions

def cont_frac(p,q): #assumes p>|q|>0
	neg = False
	if q < 0: #handle negative fractions
		neg = True
		q = -1*q
	l = []
	while q > 1:
		a = p//q + 1
		l.append(a)
		temp = q
		q = q*a - p
		p = temp
	l.append(p)
	if neg == True:
		l = [-1*e for e in l]
	return l


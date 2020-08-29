# list Brieskorn spheres that bound homology balls
# using the families in Fickle's paper

bounding_list = []

# family 1
# count = 0
# for p in range(2,100,2):
# 	for s in range(1,100,2):
# 		for k in range(0,100):
# 			if p < p*s+1  and p*s+1 < k*p*(p*s+1)+p*s-1 and k*p*(p*s+1)+p*s-1 < 100:
# 				print(p, p*s+1,k*p*(p*s+1)+p*s-1)
# 				count+=1
# print(count)

# Casson-Harer family 1
for p in range(0,100,2):
	for s in range(1,100,2):
		if p < p*s - 1 and p*s + 1 < 50 and [p, p*s - 1, p*s + 1] not in bounding_list:
			bounding_list.append([p, p*s - 1, p*s + 1])

# Casson-Harer family 2 -+
for p in range(3,100,2):
	for s in range(1,100):
		if p < p*s - 1 and p*s + 2 < 50 and [p, p*s - 1, p*s + 2] not in bounding_list:
			bounding_list.append([p, p*s - 1, p*s + 2])
			
# Casson-Harer family 2 ++
for p in range(3,100,2):
	for s in range(1,100):
		if p*s + 2 < 50 and [p, p*s + 1, p*s + 2] not in bounding_list:
			bounding_list.append([p, p*s + 1, p*s + 2])
			
# Casson-Harer family 2 --
for p in range(3,100,2):
	for s in range(1,100):
		if p < p*s - 2 and p*s - 2 < 50 and [p, p*s - 1, p*s -2] not in bounding_list:
			bounding_list.append([p, p*s - 1, p*s - 2])
			
# Casson-Harer family 2 +-
for p in range(3,100,2):
	for s in range(1,100):
		if p*s - 2 < 50 and [p, p*s + 1, p*s - 1] not in bounding_list:
			bounding_list.append([p, p*s + 1, p*s - 2])

print(len(bounding_list)) # 653 for < 100, 253 for < 50

#Stern list one ++
for s in range(1, 100,2):
	if 2*2*(2*s+1)+2*s-1 < 50 and [2,2*s+1,2*2*(2*s+1)+2*s-1] not in bounding_list:
		bounding_list.append([2,2*s+1,2*2*(2*s+1)+2*s-1])

#Stern list one --
for s in range(1, 100,2):
	if 2*2*(2*s-1)+2*s+1 < 50 and [2,2*s-1,2*2*(2*s-1)+2*s+1] not in bounding_list:
		bounding_list.append([2,2*s-1,2*2*(2*s-1)+2*s+1])

print(len(bounding_list))

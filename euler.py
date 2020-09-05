d={}
value = 1
for i in range(2,21):
	dnew={}
	print(i)
	for j in range(2,i+1):
		if i ==1 :
			break
		else:
			while i%j == 0:
				if str(j) not in dnew.keys():
					dnew[str(j)] = 1
				else :
					dnew[str(j)] = dnew[str(j)] + 1
				i = i //j
		for m in dnew.keys():
			if m in d.keys():
				if d[m] < dnew[m]:
					d[m] = dnew[m]
				else:
					pass
			else:
				d[m] = dnew[m]
for i in list(d.keys()):
	value = value*(pow(int(i) ,d[i]))
print(value , d)
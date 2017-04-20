f = open("marks.txt")
a=[]
for l in f:
	a+=[int(l.split(',')[1])]
print sum(a)/len(a)

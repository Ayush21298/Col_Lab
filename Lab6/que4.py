import sys
a=sys.argv[1]
f = open(a)
ctr=0
for l in f:
	x=l.split()
	for j in x:
		ctr+=1
print ctr

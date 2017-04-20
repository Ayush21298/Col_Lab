def lin(p,l):
	n=0
	for i in range(len(l)):
		if l[i]==p:
			print "yes, index : ",i
			n=1
	if n== 0:
		print "Not Exists"
a = input("Enter a list : ")
b = input("Enter search item :")
lin(b,a)

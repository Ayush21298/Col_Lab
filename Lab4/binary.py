def x(p,q,c):
	i=2
	while(True):
		if p != q[len(q)-i]:
			break
		c-=1
		i+=1

	

a = input("Enter a list : ")
b = input("Enter a search item : ")
count=0
while(len(a)!=0):
	l = len(a)
	if b<a[l/2]:
		a=a[0:l/2]
	elif b==a[l/2]:
		count += l/2
		x(b,a[0:(l/2)+1],count)
		break
	else : 
		a=a[l/2:]
		count+=l/2
print count

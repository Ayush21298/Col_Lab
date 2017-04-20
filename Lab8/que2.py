def d(a):
	if a==0:
		return 0
	elif a<0:
		a=-a
		return 1 + d(a/10)
	else:
		return 1 + d(a/10)




b = int(input("Enter : "))
print b
if b==0:
	print 1
else:
	print d(b)

print b
while d(b)>0:
	print b%10,
	b/=10


a = list(input("Enter a list"))
b=True
while b==True:
	b=False
	for i in range (len(a)-1):
		if a[i]>a[i+1]:
			b=True
			(a[i],a[i+1])=(a[i+1],a[i])
print a

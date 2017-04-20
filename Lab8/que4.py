def gcd(a,b):
	if a%b==0:
		return b
	else:
		a=a%b
		(a,b)=(b,a)
		return gcd(a,b)
b = int(input("Enter first : "))
c = int(input("Enter second : "))
print gcd(b,c)
	

O YEAH !!! 
def sin(x,n):
	def f(x,n):
		if n==1:
			return x
		else:
			return ((-1.0)*x*x*f(x,n-2))/(n*(n-1))
	sum=0.0
	while n>0:
		sum=sum+f(x,2*n-1)
		n-=1
	return sum
a=float(input("Enter x : "))
b=float(input("Enter n : "))
print sin(a,b)
print math.sin(a)

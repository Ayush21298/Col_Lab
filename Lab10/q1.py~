import thread
s=0

n = int(input("Enter a number : "))
k = int(input("Threads u want : "))
def sum(a,b):
	global s
	for i in range(a,b+1):
		s+=i
	return s

for i in range (0,k):
	thread.start_new_thread(sum,((i*n/k),((i+1)*n/k)))
	n=1000	
	while n>0:
		n-=1	
	print s
while 1:
	pass



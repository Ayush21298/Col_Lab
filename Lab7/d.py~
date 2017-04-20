class MemoryEXC(Exception):
	pass	
def div(a,b):
	try:
		c=a/b
		d=a**b
		if(d>20):
			raise MemoryEXC
		else:	        
			
			print c
			print d
	except ZeroDivisionError:
	        return "ZERO"
	except MemoryEXC:
		return "Memory"
a = int(input(":"))
b = int(input(":"))
print div(a,b)


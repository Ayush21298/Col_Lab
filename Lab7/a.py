def div(a,b):
	try:
	        c=a/b
	        return c
	except:
	        c="ERROR"
	else:
	        print "div:",c
	finally:
	        return 5
a = int(input(":"))
b = int(input(":"))
print div(a,b)


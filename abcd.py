import os
import time
a = "A Y U S H                P A T E L"
b=256

while(True):
	os.system("clear")
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+" "*b+a)
	b-=1
	if b<0:
		b=256
	time.sleep(0.05)

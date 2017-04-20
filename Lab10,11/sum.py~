import thread
import threading
import math
import time
tlock=threading.Lock()
sum=0
def part_sum(l,i,j):
	s=0
	for k in range(i,j):
		s+=l[k]
	print s
	tlock.acquire()
	global sum
	sum+=s
	tlock.release()


n=int(input("Enter a number : "))
l=range(1,n+1)

#print part_sum(l,0,len(l))

print l
thread.start_new_thread(part_sum,(l,0,len(l)/2))
thread.start_new_thread(part_sum,(l,(len(l)/2),len(l)))
time.sleep(1)
print sum



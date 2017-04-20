import thread
import threading
import time

def print_num (tid,N):
	tlock=threading.Lock()
	c=tid
	while(c<=N):
		print c
		c+=2
		tlock.acquire()
		time.sleep(2)
		tlock.release()

numt=0
thread.start_new_thread(print_num,(0,10))
time.sleep(1)
thread.start_new_thread(print_num,(1,10))
while 1:
	pass

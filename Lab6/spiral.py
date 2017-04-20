n=int(input("Enter a perfect square :"))
a= int(n**(0.5))
x=[]
for i in range(a):
	x+=[[]]
	for j in range(a):
		x[i]+=[0]
m=1
p=q=0
r=0
while True:
	x[p][q]=m
	m+=1
	if (r==0) and (x[p][q+1]==0) and ((q+1)<5):
		q=q+1
	elif (r==0) and (x[p][q+1]!=0)  and ((p+1)<5):
		p=p+1
		r=1
	elif (r==1) and (x[p+1][q]==0) and ((p+1)<5):
		p=p+1
	elif (r==1) and (x[p+1][q]!=0) and ((q-1)>=0):
		q=q-1
		r=2
	elif (r==2) and (x[p][q-1]==0)  and ((q-1)>=0):
		q=q-1
	elif (r==2) and (x[p][q-1]!=0) and ((p-1)>=0):
		p=p-1
		r=3
	elif (r==3) and (x[p-1][q]==0) and ((p-1)>=0):
		p=p-1
	elif (r==3) and (x[p-1][q]!=0) and ((q+1)<5):
		q=q+1
		r=0

	
for z in x:
	print z

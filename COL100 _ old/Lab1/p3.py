i=0
j=i
k=5
s=''

while i<=5 :
	j=2*i + 1 
	k=5
	s=''
	while k>i :
		s= s+' '
		k=k-1
	while j>0 :
		s = s + '*'
		j = j-1
	print(s)

	i=i+1

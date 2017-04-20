num = float(input(' Enter a number : '))
s=''
if num < 0 :
	s='negative'
elif num == 0 :
	s = 'Zero'
elif num > 0 :
	s= 'Positive'

print(s)

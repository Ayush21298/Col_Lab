num = int(input(" Enter a number "))
counter = 0;
i = 1;

while i<=num :
	d = num%i;
	if d == 0 :
		counter = counter +1
	i = i +1

if counter == 2 :
	print('YES')
else :
	print('NO') 

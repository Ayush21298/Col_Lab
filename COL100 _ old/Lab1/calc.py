num1 = input('Enter first No. : ')
num2 = input ('Enter second No. : ')

op = raw_input(' Enter the operation : ')

s = float(num1)+float(num2)
d = float(num1)-float(num2)
m = float(num1)*float(num2)
if float(num2) != 0.0:
	dv = float(num1)/float(num2)
else:
	dv = 'Not defined'


if op == '+':
	print(s)
if op == '-':
	print(d)
if op == '*':
	print(m)
if op == '/':
	print(dv)

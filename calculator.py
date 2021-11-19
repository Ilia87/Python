# calculator

what = input('What are our going to do (+ or - or *): ')

a = float(input('your first namber: '))
b = float(input('your second namber: '))

if what == '+':
	c = a + b
	print('Result ' + str(c))
elif what == '-':
	c = a - b
	print('Result ' + str(c))
elif what == '*':
	c = a * b
	print('Result ' + str(c))	
else:
	print('You are f**')



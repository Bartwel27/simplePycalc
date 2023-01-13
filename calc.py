prompt = '\n%s' % 'value==>'
prompt1 = '\n\t%s' % 'add==>'
prompt2 = '\t%s' % 'and==>'
prompt3 = '\n\t%s' % 'sub==>'
prompt4 = '\n\t%s' % 'multiply==>'
prompt5 = '\n\t%s' % 'divide==>'
print1 = '\t\t%s' % 'Simple calculator'
print2 = '\n%s' % '[1]Addition\n[2]Subtraction\n[3]Multiplication\n[4]Division'

print(print1)
print(print2)
while True:
	action = input(prompt)
	if action == '1':
		print('\n[+]Addition[+]')
		a = int(input(prompt1))
		b = int(input(prompt2))
		get = (a + b)
		print('\tget==>%s' % (get))
	elif action == '2':
		print('\n[-]Subtraction[-]')
		aSub = int(input(prompt3))
		bSub = int(input(prompt2))
		getSub = (aSub - bSub)
		print('\tget==>%s' % (getSub))
	elif action == '3':
		print('\n[*]Multiplication[*]')
		aMul = int(input(prompt4))
		bMul = int(input(prompt2))
		getMul = (aMul * bMul)
		print('\tget==>%s' % (getMul))
	elif action == '4':
		print('\n[/]Division[/]')
		aDiv = int(input(prompt5))
		bDiv = int(input(prompt2))
		getDiv = (aDiv / bDiv)
		print('\tget==>%s' % (getDiv))
	elif action == 'exit':
		while True:
			break
		break
		
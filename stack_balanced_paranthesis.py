'''
Use a stack to check whether or not a string has balanced usage of parenthesis.
Example:
() , (()), {[()]} -> Balanced Parethesis
((), {{}}] , [][]]-> Not Balanced
'''

from stack import Stack

def match(p1,p2):
	if p1 == '(' and p2 ==')':
		return True
	elif p1 == '[' and p2 ==']':
		return True
	elif p1 == '{' and p2 == '}':
		return True
	else:
		return False

def is_paren_balan(paren_string):
	s = Stack()
	balanced = True
	index = 0

	while index < len(paren_string) and balanced:
		current_paren = paren_string[index]
		if current_paren in ['(','[','{']:
			s.push(current_paren)

		elif current_paren in [')',']','}']:
			if s.is_empty():
				balanced= False

			else:
				if match(s.pop(),current_paren):
					balanced = True
				else:
					balanced = False

		index +=1
	if s.is_empty() and balanced == True:
		return 'Balanced String'
	else:
		return 'Not Balanced'

print(is_paren_balan('][][]{{}}'))


from stack import *

def reverse_string(stack, input_str):
	for i in range(len(input_str)):
		stack.push(input_str[i])

	rev_str = ''
	while not stack.is_empty():
		rev_str += stack.pop()

	return rev_str

input_str = "Hello"
stack = Stack()

print(reverse_string(stack, input_str))

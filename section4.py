def comparison():
	print(f'True true: {True} {not False}')
	
def chaining():
		print(f'True: {1 < 2 and 2 == 2 and not False}')
		print('True: {one}, True: {two}, True: {three}'.format(one = False or True, two = not False and True, three = False or not False and True))
		print(f'Comparison chaining: {2 < 3 < 4 > 3 == 3.0}')
		pi = 3.14# case sensitive
		print(f'3.1 < Pi < 3.2 {3.1 < pi < 3.2}')
	
	
if __name__ == '__main__':
	print("Hello from Section 4!")
def methodsAndDocumentation():
	'''
	DOCSTRING: is this the docstring?
	Is very good
	Takes no prisoners
	Returns when done'''
	
def functionA(meaning = 42):
	if meaning == 42:
		print("But what is the question?")
	else:
		print(f'The meaning is {meaning}')
	return meaning
	
def isDogInString(string):
	if len(string) == 0:
		return False
	return 'dog' in string.lower()
	
def pigLatin(string):
	'''	If word start with a vowel, ad "ay" to ends
	Otherwise put first letter at end and add "ay" '''
	vowels = 'aeiouy'
	result = ''
	for word in string.split():
		if word[0] in vowels:
			result += word + 'ay'
		else:
			result += word[1:] + word[0] + 'ay'
		result += ' '
	return result[:-1]
	
if __name__ == '__main__':
	print("Methods and functions")
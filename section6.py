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
	
def varArgs(*argumentTuple):
	print(type(argumentTuple), sum(argumentTuple))
	
def keyWordArguments(**kwargs):
	print(type(kwargs))
	if 'tool' in kwargs:
		print(f"Use a {kwargs['tool']}")
	else:
		print("No tools!")
		
def argumentation(*args, **kwargs):
	print("A ratio {num} and liquid {}".format(kwargs['liquid'], num = args[1]))
	
def skyline(input):
#From: https://stackoverflow.com/questions/3678869/pythonic-way-to-combine-two-lists-in-an-alternating-fashion
#list3 = [sub[i] for i in range(len(list2)) for sub in [list1, list2]] + [list1[-1]]
	low = input[::2].lower()
	upp = input[1::2].upper()
	both = []
	for index in range(len(low)):
		both.append(low[index])
		if index < len(upp):
			both.append(upp[index])
	return ''.join(both)
	
'''LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers 
if both numbers are even, but returns the greater if one or both numbers are odd'''
def lesser_of_two_evens(a, b):
	if(a % 2 == 0) and (b % 2 == 0):
		return min(a, b)
	else:
		return max(a, b)
		
'''ANIMAL CRACKERS: Write a function takes a two-word string and 
returns True if both words begin with same letter'''
def animal_crackers(input):
	words = input.split()
	return words[0][0].lower() == words[1][0].lower()
	
'''MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 
or if one of the integers is 20. If not, return False'''
def makes_twenty(a, b):
	return (a == 20) or (b == 20) or (a + b == 20)
	
'''OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name'''
def old_macdonald(name):
	if len(name) < 4:
		return ''
	capList = list(name)
	capList[0] = capList[0].upper()
	capList[3] = capList[3].upper()
	return ''.join(capList)
	
'''MASTER YODA: Given a sentence, return a sentence with the words reversed'''
def master_yoda(sentence):
	words = sentence.split()
	reversed = [w +' ' for w in words[:0:-1]]
	# print('*',reversed, '*', words[0], '*')
	reversed.append(words[0])
	return ''.join(reversed)
	
'''ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200'''
def almost_there(n):
	return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)
	
'''Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.'''
def has_33(ints):
	found = False
	for num in ints:
		if not num == 3:
			found = False
		elif found and (num == 3):
			return True
		elif num == 3:
			found = True
	return False

'''PAPER DOLL: Given a string, return a string where for every character in the original 
there are three characters'''
def paper_doll(string):
	tripple = [x*3 for x in string]
	return ''.join(tripple)
	
'''BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, 
return their sum. If their sum exceeds 21 and there's an eleven, 
reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST' '''
def blackjack(a, b, c):
	sum = a+b+c
	thereIsAnEleven = (a == 11) or (b == 11) or (c == 11)
	if (sum > 21) and thereIsAnEleven:
		sum -= 10
	if (sum < 21):
		return sum
	else:
		return 'BUST'
		
'''SUMMER OF '69: Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 and extending to the next 9 
(every 6 will be followed by at least one 9). Return 0 for no numbers.'''
def summer_69(numbers):
	sum = 0
	ignore = False
	for num in numbers:
		if num == 6:
			ignore = True
			continue
		if num == 9:
			ignore = False
			continue
		if not ignore:
			sum += num
	return sum
	
'''SPY GAME: Write a function that takes in a list of integers and returns 
True if it contains 007 in order
e.g.  [0,1,0,2,7] -> True'''
def spy_game(integers):
	filtered = [x  for x in integers if x == 0 or x == 7]
	last = len(filtered) - 2#maximum length including first 0
	if last < 1:
		return False
	bondFound = False
	for x in range(last):
		if (filtered[x] == 0) and (filtered[x + 1] == 0) and (filtered[x + 2] == 7):
			bondFound = True
			break
	return bondFound
'''Return a list of all primes up to and including 'number' '''
def makePrimes(num):
	allNums = [x for x in range(num)]
	primes = []
	for x in range(2, num):
		if allNums[x] == 0:
			continue
		else:
			primes.append(x)
		for y in range(x, num, x):
			allNums[y] = 0
			
	return primes
	
'''COUNT PRIMES: Write a function that returns the number of prime numbers that 
exist up to and including a given number'''
def count_primes(number):
#Make a list of all primes up to and including 'number'
	primeCount = makePrimes(number)
#Return length of list
	return len(primeCount)
font = {'a': '\
  a  \n\
 a a \n\
aaaaa\n\
a   a\n\
a   a\n'}
'''PRINT BIG: Write a function that takes in a single letter, 
and returns a 5x5 representation of that letter'''
def print_big(letter):
	print(font[letter])
	
if __name__ == '__main__':
	print("Methods and functions")
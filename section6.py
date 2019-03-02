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
	words = input.lower().split()
	return words[0][0] == words[1][0]
	
'''MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 
or if one of the integers is 20. If not, return False'''
def makes_twenty(a, b):
	return (a == 20) or (b == 20) or (a + b == 20)
	
'''OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name'''
def old_macdonald(name):
	if len(name) < 4:
		return ''
	# capList = list(name)
	# capList[0] = capList[0].upper()
	# capList[3] = capList[3].upper()
	# return ''.join(capList)
	first = name[:3].capitalize()
	fourth = name[3:].capitalize()
	return first + fourth
	
'''MASTER YODA: Given a sentence, return a sentence with the words reversed'''
def master_yoda(sentence):
	# words = sentence.split()
	# reversed = [w +' ' for w in words[:0:-1]]
	# reversed.append(words[0])
	# return ''.join(reversed)
	reversed = sentence.split()[::-1]
	return ' '.join(reversed)
	
'''ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200'''
def almost_there(n):
	return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)
	
'''Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.'''
def has_33(ints):
	# found = False
	# for num in ints:
		# if not num == 3:
			# found = False
		# elif found and (num == 3):
			# return True
		# elif num == 3:
			# found = True
	# return False
	for a in range(len(ints) - 1):
		if (ints[a] == 3) and (ints[a + 1] == 3):
			return True
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
	if (sum <= 21):
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
	# filtered = [x  for x in integers if x == 0 or x == 7]
	# last = len(filtered) - 2#maximum length including first 0
	# if last < 1:
		# return False
	# bondFound = False
	# for x in range(last):
		# if (filtered[x] == 0) and (filtered[x + 1] == 0) and (filtered[x + 2] == 7):
			# bondFound = True
			# break
	# return bondFound
	'''This implementation will crash if 666 is included in 'integers' '''
	code = [0,0,7,666]#666 ensures code[0] always can be referenced
	for num in integers:
		if num == code[0]:
			code.pop(0)
	return len(code) == 1
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
	
def consumer(x):
	return 2 * x
def consumer2(x, y):#No function overloading
	return y * x
	
def mapFunc():
	nums = [1,2,3,4,5]
	othernums = map(consumer, nums)
	# print(othernums[0]) //TypeError: 'map' object is not subscriptable
	#map returns an iterator
	print(tuple(othernums))
	for item in othernums:
		print(item)
	arg1 = [1,2,3]
	arg2 = [1,10,100]
	print(list(map(consumer2,arg1,arg2)))
	
def is_good(x):
	return x == 42
	
def filterFunc():
	filtered = filter(is_good, [1,2,42,3,4,42])
	print([x for x in filtered])
	
def laLaLambda():
	print([i for i in map(lambda num : num ** 2, [1,2,3])])
	for i in filter(lambda q : q%2 == 0, [1,2,3,4,5,6,7,8,9]):
		print(i)
'''Write a function that computes the volume of a sphere given its radius'''
def assignment_sphere(radius):
	from math import pi
	return 4*pi*radius**3/3
	
'''Write a function that checks whether a number is in a given range (inclusive of high and low)'''
def ran_check(num,low,high):
	return low <= num <= high
	
'''Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.'''
def up_low(s):
	upper = 0
	lower = 0
	for c in s:
		if c.isupper():
			upper += 1
		elif c.islower():
			lower += 1
	return (upper, lower)
	
'''Write a Python function that takes a list and returns a new list with unique elements of the first list.'''
def unique_list(lst):
	return list(set(lst))
	
'''Write a Python function to multiply all the numbers in a list.'''
def multiply(numbers):
	mul = 1
	for x in numbers:
		mul *= x
	return mul
'''Write a Python function that checks whether a passed in string is palindrome or not.
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.'''
def palindrome(s):
	#Handle spaces
	filtered = reversed = [c for c in filter(lambda c: c!= ' ', s)]
	reversed.reverse()
	return filtered == reversed
	#Handle odd and even length
	
'''Write a Python function to check whether a string is pangram or not.

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"'''
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
	uniq = set(str1)
	for letter in alphabet:
		if not letter in uniq:
			return False
	return True

if __name__ == '__main__':
	print("Methods and functions")
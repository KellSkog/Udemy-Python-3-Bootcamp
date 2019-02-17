def controlflow():
	aBoolean = False
	if aBoolean == True:
		print('True')
	elif aBoolean == False:
		print('False')
	else:
		print("Not a boolean")
		
def forLoop():
	aList = [1,2,3,4,5,6,7,8]
	for num in aList:
		if num % 2 == 0:
			print(num)
	i = 0
	tot = 0
	for i in aList:
		tot += i
	print(f'Total (4*9): {tot}')
	
	for _ in '_':
		print('Unused var _')
	for i in ('abc'):
		print(f'Tuple member {i}')
	listOfTuples = [(1, 2), (3, 4), (5, 6)]
	print('Tuple Unpacking')
	for a, b in listOfTuples:
		print(a)
		print(b)
	
	print("Iterating thru a dictionary")
	aDict = {1:'a', 2:'b', 3:'c'}
	for key, val in aDict.items():#items return tuples with k, v pairs
		print(f'Key: {key} : Value {val}')#With Tuple unpacking we get keys and values
		
def whileLoop():
	print("While loops")
	var = 3
	while var > 0:
		print(var)
		var -= 1
	else:
		print("While terminated")
		
	counters = {'outer':0, 'inner':0}#Dictionary
	#Ok ok break and continue are ill suited for while loops
	while counters['outer'] < 10:
		if counters['outer'] == 5: break
		if counters['outer'] == 2: 
			counters['outer'] += 1
			continue
		counters['inner'] = 0
		while counters['inner'] < 10:
			if counters['inner'] % 2 == 0: 
				counters['inner'] += 1
				continue
			if counters['inner'] == counters['outer']: break
			print(f"Outer {counters['outer']}, Inner {counters['inner']}")
			counters['inner'] += 1
		counters['outer'] += 1

def usefulOperators():
	start = 1
	stopExclusive = 5
	stepSize = 2
	print('range() is a generator of integers')
	for x in range(start, stopExclusive, stepSize):
		print(x)
	aList = list(range(start, stopExclusive, stepSize))
	for x in aList:
		print(x)
		
	print('Enumerate generates tuples with enumerated values')
	word = 'Hello'
	for index, value in enumerate(word):#Using tuple unpacking
		print(index, value)
	
	print('Zip generates a list of tuples combined from two lists')
	list1 = "ABS"
	list2 = [0, 1, 2]
	for item in zip(list2, list1):
		print(item)
	myDic = dict(zip(list2, list1))
	for k,v  in myDic.items():
		print(k, v)
		
	print("In operator returns true if an item is in a list")
	print(f'True: {"B" in list1} False: {5 in list2}')
	print(f'1 is a key of myDic: {1 in myDic}')
	print(f'Min {min(list2)}, Max {max(list2)}')
	
	print("Shuffle randomizes in place")
	from random import shuffle
	list1 = list(range(10))
	shuffle(list1)
	print(list1)
	
	print("Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1)")
	from random import randint, randrange
	for rnd in range(5):
		print(randint(1, 2), randrange(1, 3))
		
	userInput = input("aNumber")
	if userInput.isnumeric():
		print(f'Is numeric {int(userInput)}')
	else:
		print(f'Is not numeric {userInput}')
				
def listComprehension():
	print("List comprehension builds lists less verbose, not more efficiently")
	list1 = []
	for x in range(10):
		list1.append(x)
	print(list1)
	print("The comprehension itself")
	myDic = dict(zip([0, 1, 2, 3, 4, 5], 'abcdef'))
	listComp = [value.upper() for key, value in myDic.items() if value !='c']
	print(listComp)
	
	print("Up the ante if else")
	listComp = [value.upper() if value == 'a' else value for key, value in myDic.items() if value !='c']
	print(listComp)
	
	print("Up the ante another notch, nested loops")
	list1 = [outer * inner for outer in [1,2,3] for inner in [1, 10, 100]]
	print (list1)
	
def assessment():
	print("Use for, .split(), and if to create a Statement that will print out words that start with 's':")
	st = 'Print only the words that start with s in this sentence'
	onlyS = [word for word in st.split() if word[0].upper() == 'S']
	print(onlyS)
	for word in st.split():
		if word[0].upper() == 'S':
			print(word)
	
	print("Use range() to print all the even numbers from 0 to 10.")
	for even in range(0, 11, 2):
		print(even)
	
	print("Use a List Comprehension to create a list of all numbers between 1 \
	and 50 that are divisible by 3.")
	divBy3 = [num for num in range(1, 52) if num%3 == 0]
	print(divBy3)
	divBy3 = [num for num in range(3, 52, 3)]
	print(divBy3)
	
	print('Go through the string below and if the length of a word is even print "even!"')
	st = 'Print every word in this sentence that has an even number of letters'
	for word in st.split():
		if len(word)%2 == 0:
			print('even')
			
	print('Write a program that prints the integers from 1 to 100. \
	But for multiples of three print "Fizz" instead of the number, \
	and for the multiples of five print "Buzz". \
	For numbers which are multiples of both three and five print "FizzBuzz".')
	for num in range(1, 101):
		if num%3 == 0 and num%5 == 0:
			print('FizzBuzz')
		elif num%3 == 0:
			print('Fizz')
		elif num%5 == 0:
			print('Buzz')
		else:
			print(num)
	
	print("Use List Comprehension to create a list of the first letters of every word in the string below:")
	st = 'Create a list of the first letters of every word in this string'
	acronym = [word[0] for word in st.split()]
	print(acronym)
		
def dohickey():
	pass
if __name__ == '__main__':
	print("Statements")
	print("If, for, while, Operators, List Comprehensions and a test")
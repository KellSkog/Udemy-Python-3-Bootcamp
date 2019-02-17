#Numbers are either integer or float
#Strings are ordered sequences of character
#Lists are ordered sequences of objects
#Tuples are imutable ordered sequences of objects
#Dictionaries are mutable unordered sequences of maps (key-value pairs)
#Sets are imutable unordered sequences of unique objects
def numbers():
#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25
	equation = 2 * 240 / 6 + 3**3 - 6.75
	print(equation)
#What is the type of the result of the expression 3 + 1.5 + 4?
# float
	print(type(3 + 1.5 + 4))

	nums = 'ints are at least {max}'
	print(nums.format(max=2**69))
	
#What would you use to find a number’s square root, as well as its square?
	import math
	print(f'Square root of 64: {math.sqrt(64)}, 5 squared: {math.pow(5, 2)} or {5**2}')
	print(f'Square root of 64 can also be written as 2 ** 0.5 {2 ** 0.5}')
	
def strings():
#Given the string 'hello' give an index command that returns 'e'
	str = 'hello'
	print(str[1])
#Reverse the string 'hello' using slicing
	print(str[::-1])
	
#Given the string hello, give two methods of producing the letter 'o' using indexing
	print(f'First: {str[4]}, second {str[-1]}')
	
def lists():
#Build this list [0,0,0] two separate ways
	list1 = [0, 0, 0]
	list2 = [0]
	list2.append(0)
	list2.append(0)
	print(f'Way 1: {list1}, way 2: {list2}')
	print(f'Elements can be multiplied [0] * 3: {[0]*3}')
	
#Reassign 'hello' in this nested list to say 'goodbye' instead
	list3 = [1,2,[3,4,'hello']]
	print(list3)
	list3[2][2] = 'goodbye'
	print(list3)
	
#Sort the list below
	list4 = [5,3,4,6,1]
	list4.sort()
	list5 = [5,3,4,6,1].sort() #Return nothing
	print(f'Correct: {list4}, Incorrect: {list5}')
	print(f'Not in place sorting but returns a sorted object: {sorted([5,3,4,6,1])}')
	
def dictionaries():
#Using keys and indexing, grab the 'hello' from the following dictionaries
	d = {'simple_key':'hello'}
# Grab 'hello'
	print(d['simple_key'])
	d = {'k1':{'k2':'hello'}}
# Grab 'hello'
	print(d['k1']['k2'])
# Getting a little tricker
	d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello
	print(d['k1'][0]['nest_key'][1][0])
	
# This will be hard and annoying!
	d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
	print(f"hard and annoying! {d['k1'][2]['k2'][1]['tough'][2][0]}")
	
#Can you sort a dictionary? Why or why not?
#Dictionaries are unordered maps, and sorting implies order, so no!
#Normal dictionaries are mappings not sequences, orderedDictionare can be sorted

def tuples():
#What is the major difference between tuples and lists?
#Lists are mutable, tuples are not
#How do you create a tuple?
	tupp = (1, 2, 3)
	print(tupp[1])
	#tupp[1] = 42#Illegal!
	print(tupp[1])#TypeError: 'tuple' object does not support item assignment
	
def sets():
#What is unique about a set?
#Sets has no duplicate members, only unique values
	sett = {1,1,2,2,3,3}
	print(sett)# {1, 2, 3}
#Is it mutable?
#	sett[0] = 3;#It is unordered...
#TypeError: 'set' object does not support item assignment

#Use a set to find the unique values of the list below:
	list5 = [1,2,2,33,4,4,11,22,3,3,2]
	set2 = set(list5)
	print(set2)
	
def booleans():
#What will be the resulting Boolean of the following pieces of code
	print(f'False: {2 > 3}')
	print(f'False: {3 <= 2}')
	print(f'False: {3 == 2.0}')
	print(f'Probably true: {3.0 == 3}')
	print(f'False (sqrt(4) == 2.0: {4**0.5 != 2}')
#Final Question: What is the boolean output of the cell block below?
# two nested lists
	l_one = [1,2,[3,4]]
	l_two = [1,2,{'k1':4}]

# True or False?
	
	print(f"False 3>=4: {l_one[2][0] >= l_two[2]['k1']}")
	
	
if __name__ == '__main__':
	print('Assesses Objects and Data structures')
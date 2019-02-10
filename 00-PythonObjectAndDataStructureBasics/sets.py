def upset():
	mySet = {1, 5, 3, 4, 4, 1}
	print(f'mySet: {mySet}')
	otherSet = set()
	#also check object creation for other types
	aList = list()
	aDict = dict()
	aTuple = tuple()
	aSet = set()
	print(f'List: {aList}, Dict {aDict}, Tuple {aTuple}, Set: {aSet}, set type {type(aSet)}')
	
	otherSet.add(3)
	otherSet.add(2)
	otherSet.add(1)
	otherSet.add(1)
	print(f'Added 3,2,1,1: {otherSet}')
	
	thirdSet = set([1, 1, 1, 3, 3, 3, 2, 2, 2])
	print(f'set Constructor with list: {thirdSet}')
if __name__ == '__main__':
	print('Sets say hello!')
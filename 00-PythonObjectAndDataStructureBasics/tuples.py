def tupp():
	myTupence = (1, 2, 3, 2, 2)
	print(f"myTupence {myTupence}")
	print(f"Type {type(myTupence)} Length {len(myTupence)} Count of 2: {myTupence.count(2)}")
	myTupence = ('a', 4, 3.14)
	#myTupence[1] = 5 #TypeError: 'tuple' object does not support item assignment
	print(f'Index of Pi: {myTupence.index(3.14)} Again: {myTupence[-1]}')
	
if __name__ == "__main__":
	print('Tuples says hello!')

# f'..' requires python 3.6
def concatenate():
	alfa = ['a', 'b']
	num = [1, 2]
	print(f'Concatenated {alfa + num}')
	alfanum = alfa
	alfanum.append(num.pop())
	alfanum.append(num.pop())
	print('Concat reversed {val}'.format(val = alfanum))
	print(f'Empty {num}')
	
	myUnsorted = [5,3,7,2,0,9,1]
	myUnsorted.sort()#myUnsorted is now sorted, sort returns 'None'
	print(f'Sorted {myUnsorted}')
	myUnsorted.reverse()
	print('Reversed {val}'.format(val = myUnsorted))
	
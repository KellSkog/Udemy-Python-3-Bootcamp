def concatenate():
	alfa = ['a', 'b']
	num = [1, 2]
	print(alfa + num)
	alfanum = alfa
	alfanum.append(num.pop())
	alfanum.append(num.pop())
	print(alfanum)
	print(num)
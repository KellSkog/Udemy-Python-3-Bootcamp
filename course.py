import section6

if __name__ == "__main__":
	#section6.methodsAndDocumentation()
	# section6.functionA(42)
	# section6.functionA()
	# print(f'Got {section6.functionA(3.14)}')
	
	# print(f"Dog? {section6.isDogInString('only cats in this one')}")
	# print(f"Dog? {section6.isDogInString('this one has a small dog')}")
	
	# print(section6.pigLatin('word'))
	# print(section6.pigLatin('apple'))
	# print(section6.pigLatin('apple word apple'))
	
	# section6.varArgs(1,2,3,4,5)
	# section6.keyWordArguments(tool= 'hammer')
	
	# section6.argumentation(0, 3.14, 'Hello', element = 'Boron', liquid = 'water', cost = 5)
	# print(section6.skyline('Hello world'))
	
	assert section6.lesser_of_two_evens(2, 4) == 2
	assert section6.lesser_of_two_evens(6, 4) == 4
	assert section6.lesser_of_two_evens(2, 1) == 2
	assert section6.lesser_of_two_evens(1, 2) == 2
	assert section6.lesser_of_two_evens(3, 5) == 5
	
	assert section6.animal_crackers('Levelheaded Llama')
	assert not section6.animal_crackers('Crazy Kangaroo')
	
	assert section6.makes_twenty(20, 5)
	assert section6.makes_twenty(5, 20)
	assert section6.makes_twenty(10, 10)
	assert not section6.makes_twenty(5, 5)
	assert section6.makes_twenty(20, 20)
	
	assert section6.old_macdonald('macdonald') == 'MacDonald'
	
	assert section6.master_yoda('I am home') == 'home am I'
	assert section6.master_yoda('We are ready') == 'ready are We'
	
	assert section6.almost_there(90) == True
	assert section6.almost_there(104) == True
	assert section6.almost_there(150) == False
	assert section6.almost_there(209) == True
	
	assert section6.has_33([1, 3, 3]) == True
	assert section6.has_33([1, 3, 1, 3]) == False
	assert section6.has_33([3, 1, 3]) == False
	
	assert section6.paper_doll('Hello') == 'HHHeeellllllooo'
	assert section6.paper_doll('Mississippi') == 'MMMiiissssssiiissssssiiippppppiii'
	
	assert section6.blackjack(5,6,7) == 18
	assert section6.blackjack(9,9,9) == 'BUST'
	assert section6.blackjack(9,9,11) == 19
	
	assert section6.summer_69([1, 3, 5]) == 9
	assert section6.summer_69([4, 5, 6, 7, 8, 9]) == 9
	assert section6.summer_69([2, 1, 6, 9, 11]) == 14
	assert section6.summer_69([6, 7, 8, 9]) == 0
	
	assert section6.spy_game([1,2,4,0,0,7,5]) == True
	assert section6.spy_game([1,0,2,4,0,5,7]) == True
	assert section6.spy_game([1,7,2,0,4,5,0]) == False
	
	assert section6.count_primes(100) == 25
	
	section6.print_big('a')
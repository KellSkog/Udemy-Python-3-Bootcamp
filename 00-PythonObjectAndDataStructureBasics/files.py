def openWith():
	with open(path + "myTextfile.txt", mode = 'r+') as file:
		txt = file.read()
		file.seek(0)
		txt2 = file.read()
		print(f'Equals: {txt[5] == txt2[5]}')
	# file closed
def openNormal():
	path = 'C:\\Users\\Kell Skog\\Repositories\\Udemy-Python-3-Bootcamp\\00-PythonObjectAndDataStructureBasics\\'
	file = open(path + "myTextfile.txt")
	txt = file.readlines()
	for string in txt:
		print(string)
	file.close()
	
def overWriting():
	with open("blah.txt", mode = 'w') as file:
		file.write('blah blah blah')
	with open("blah.txt", mode = 'w') as file:
		file.write('yadyadayada')
	with open("blah.txt", mode = 'r') as file:
		content = file.read()
	if content[3] == 'y':
		print('Equal')
	else:
		print('Not overwritten')
def appending():
	with open("blah.txt", mode = 'a') as file:
		file.write('1101010011010010')
	with open("blah.txt", mode = 'r') as file:
		print(file.read())
		
def textFile():
	#openWith()
	#openNormal()
	#overWriting()
	appending()
	
	
	
	
if __name__ == "__main__":
	print("Hello from Files!")

#File open modes
# r - read only
# w - write only new or replace
# a - append only
# r+ -read and write
# w+ -New or replace and read
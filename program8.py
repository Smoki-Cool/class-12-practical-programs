# Write a python program to read and display file content line by
# line with each word separated by ‘*’


with open('/storage/emulated/0/Documents/Pydroid3/text.txt') as file:
	for line in file.readlines():
		for word in line:
			print(word, end="*")

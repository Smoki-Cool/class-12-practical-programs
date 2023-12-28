# Write a python program to read the content of the file and display total numbers of 
# upper case and lower case characters.


with open('/storage/emulated/0/Documents/Pydroid3/text.txt') as file:
	upper = 0
	lower = 0
	for char in file.read():
		if char.isupper():
			upper += 1
		elif char.isalpha():
			lower += 1
			
	
	print("Uppercase:", upper)
	print("Lowercase:", lower)

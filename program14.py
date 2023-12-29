# Write a program to know the cursor position and print the text according to the below given specifications:
# 1. Print the initial position
# 2. Move the cursor to 4th position
# 3. Display next 5 characters
# 4. Move cursor to next 10 characters

def pos(file): return file.tell()

with open("text.txt") as file:
	print(pos(file))
	
	file.seek(4)
	
	print(file.read(5))
	
	file.seek(pos(file) + 10)

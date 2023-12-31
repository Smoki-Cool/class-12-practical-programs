# Write a python program to read the content of the file line by line and write it to
# another file except for the lines that contain ‘o’ letter in it.

with open("text.txt") as file1:
	with open("copy.txt", "w") as file2:
		count = 0
		for line in file1.readlines():
			if 'o' not in line.lower():
				file2.write(line)
				count += 1
		
	print("Wrote", count, "lines to file2.")

print("\nContents of file2:")

with open("copy.txt") as file2:
	for line in file2.readlines():
		print(line, end='')

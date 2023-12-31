# Write a python program to read and display file content line by
# line with each word separated by ‘*’

with open('text.txt') as file:
    for line in file.readlines():
        for word in line.split():
            print(word, end="*")
        print()

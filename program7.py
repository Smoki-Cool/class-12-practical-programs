# Write a python program to search any word in given string/sentence. User provides 
# input string/sentence and the word to search.

import re


def search(sentence, word):
	s = re.search(r"\b{0}".format(word), sentence)
	
	if s:
	 	mark(s.start(), word, sentence)
	else:
	 	print("No results found.")


def mark(start, word, sentence):
	print()
	print(sentence)
	print(" "*start + "^"*len(word))


sentence = input("Enter your sentence: ")
word = input("Enter the word to search for: ")

search(sentence, word)

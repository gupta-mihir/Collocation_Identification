import sys
import re

def is_unigram(word):
    if len(word) < 2 and len(word) > 0 and word.isalnum():
        return True
    elif len(word) < 2 and len(word) > 0 and word.isalnum() == False:
        return False
    else:
        return True

def is_bigram():
    print('Method used to find if the word is a bigram')

def chi_sq():
    print('This does the chi squared methods')

def pmi():
    print('this does the pmi method of calculations')

unigram = {}
bigram = {}

chi_sq()
pmi()

file_name = sys.argv[1]

file_train = open(file_name, "r")
lines = file_train.readlines()

for i in range(len(lines)):
		# remove the \n at the end.
	s = lines[i].strip()

		# split the line into a list, [id, str, classification]
	lst = s.split()

		# remove the first element, since it's not used.
	#lst.pop(0)

		# Now assign the cleaned line back into the lines list.
	lines[i] = lst

for i in range(20):
    for j in range(len(lines[i])):
       word = lines[i][j]
       if is_unigram(word):
        if word in unigram:
            unigram[word] += 1
        else:
            unigram[word] = 1 
print(unigram)
import sys
import math
import numpy as np


def is_unigram(word):
    if len(word) < 2 and len(word) > 0 and word.isalnum() or word == '$' or word == '%':
        return True
    elif len(word) < 2 and len(word) > 0 and word.isalnum() == False and word != '$' and word != '%':
        return False
    else:
        return True

def is_bigram(word_1, word_2):
    if word_1 in unigram and word_2 in unigram:
        return True
    else:
        return False

unigram = {}
bigram = {}

def chi_sq(both_word):
    str_split = both_word.split()
    word_1 = str_split[0]
    first = word_1
    word_2 = str_split[1]
    last = word_2
    count_both = bigram[both_word]
    count_first= unigram[first]
    #print('LOOK HERE')
    #print(word_1)
    #print(count_first)
    
    count_last= unigram[last]
    #print(count_last)
    #print(bi_counter)
    count_rest = bi_counter - count_first - count_last - count_both
    #print(count_rest)
    #EXPECTED
    e_quad_11 = (((count_first / bi_counter) * (count_last / bi_counter)) * bi_counter)
    e_quad_12 =  ((((count_first + count_rest) / bi_counter) * ((count_first) / bi_counter)) * bi_counter)
    e_quad_21 = ((((count_last + count_rest) / bi_counter) * ((count_last) / bi_counter)) * bi_counter)
    e_quad_22 = ((((count_last + count_rest) / bi_counter) * ((count_first + count_rest) / bi_counter)) * bi_counter)
    #OBSERVED VALUES - EXPECTED WHOLE SQUARED DIVIDED BY EXPECTED
    chi_11 = ((count_both - e_quad_11) * (count_both - e_quad_11)) / e_quad_11
    chi_12 = ((count_first - e_quad_12) * (count_first - e_quad_12)) / e_quad_12
    chi_21 = ((count_last - e_quad_21) * (count_last - e_quad_21)) / e_quad_21
    chi_22 = ((count_rest - e_quad_22) * (count_rest - e_quad_22)) / e_quad_22

    total_score = chi_11 + chi_12 + chi_21 + chi_22
    return total_score



def pmi(both_word):
    str_split = both_word.split(' ')
    word_1 = str_split[0]
    word_2 = str_split[1]
    count_1 = unigram[word_1]
    count_2 = unigram[word_2]
    count_both = (bigram[both_word])
    prob_both = count_both / counter
    prob_word_1 = count_1 / counter
    prob_word_2 = count_2 / counter
    prod_word = prob_word_1 * prob_word_2
    answer = math.log2(prob_both / prod_word )
    return answer




#chi_sq()


file_name = sys.argv[1]
measure = sys.argv[2]


file_train = open(file_name, "r")
lines = file_train.readlines()

for i in range(len(lines)):
		# remove the \n at the end.
	s = lines[i].strip()

		# split the line into a list, [id, str, classification]
	lst = s.split()

		# Now assign the cleaned line back into the lines list.
	lines[i] = lst
bi_counter = 0

counter = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        counter += 1

for i in range(len(lines)):
    for j in range(len(lines[i])):
       word = lines[i][j]
       if is_unigram(word):
        if word in unigram:
            unigram[word] += 1
        else:
            unigram[word] = 1 

for i in range(len(lines)):
    if i != len(lines) - 1:

        word_next = lines[i+1][0]
    else:
        word_next = 'NULL'
    for j in range(len(lines[i])):
        word_1 = lines[i][j]
        if j != len(lines[i]) - 1:
            word_2 = lines[i][j+1]
        else:
            word_2 = word_next
        if is_bigram(word_1, word_2):
            bi_counter += 1
            bi_word = word_1 + ' ' + word_2
            if bi_word in bigram:
                bigram[bi_word] += 1
        else:
            bigram[bi_word] = 1 


if measure == "PMI":
    pmi_results = []
    pmi_dict = {}
    for key in bigram:
        pmi_results.append([key, pmi(key)])
        pmi_dict[key] = pmi(key)

    pmi_results.sort(key=lambda x: x[1])

    pmi_results.reverse()

    final_results_pmi = pmi_results[:20]
    print("PMI RESULTS")
    print("TOP 20 SCORES")
    for iter in range(20):
        if iter < 9:
            print(f"Bigram{iter+1} Score{iter+1}:   {final_results_pmi[iter]}")
        else:
            print(f"Bigram{iter+1} Score{iter+1}: {final_results_pmi[iter]}")
elif measure == "chi-square":
    chi_results = []
    chi_dict = {}
    for key in bigram:
        chi_results.append([key, chi_sq(key)])
        chi_dict[key] = chi_sq(key)

    chi_results.sort(key=lambda x: x[1])

    chi_results.reverse()

    final_results_chi = chi_results[:20]
    print("CHI SQUARED RESULTS")
    print("TOP 20 SCORES")
    for iter in range(20):
        if iter < 9:
            print(f"Bigram{iter+1} Score{iter+1}:   {final_results_chi[iter]}")
        else:
            print(f"Bigram{iter+1} Score{iter+1}: {final_results_chi[iter]}")
            
        #print(final_results_chi)




#TESTING / DEBUGGING

#print(bigram)
#print(pmi_results)
#print(pmi_dict)
print('Above is the answer')

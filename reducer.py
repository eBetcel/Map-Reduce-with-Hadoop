#!/usr/bin/env python
import sys
from decimal import Decimal

highest_incomes = []

# curr_count = 0
# Process each key-value pair from the mapper
for line in sys.stdin:
    # Get the key and value from the current line
    line = line.split("\t")
    nome, salario = line[0].split(",")
    salario = Decimal(salario)
    print(salario)
    # print(highest_icomes)
    # Convert the count to an int
    # count = int(count)
    # If the current word is the same as the previous word,
    # increment its count, otherwise print the words count
    # to stdout
#   if word == curr_word:
#     curr_count += count
#   else:
#     # Write word and its number of occurrences as a key-value
#     # pair to stdout
#     if curr_word:
#       print ('{0}\t{1}'.format(curr_word, curr_count))
#     curr_word = word
#     curr_count = count
# # Output the count for the last word
# if curr_word == word:
#   print ('{0}\t{1}'.format(curr_word, curr_count))

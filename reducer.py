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

    if(len(highest_incomes) < 11):
      highest_incomes.append((nome, salario))

    else:
      highest_incomes.append((nome, salario))
      highest_incomes = sorted(highest_incomes, key = lambda x: x[1], reverse=True)
      highest_incomes.pop()

      

print(highest_incomes[:-1])
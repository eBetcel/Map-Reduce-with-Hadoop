#!/usr/bin/env python
import sys
from decimal import Decimal

highest_incomes = []

for line in sys.stdin:
    # Get the each pair
    line = line.split("\t")
    nome, salario = line[0].split(",")
    salario = Decimal(salario)

    # Populate list with fisrt 11 values
    if len(highest_incomes) < 11:
        highest_incomes.append((nome, salario))

    # Add a new value, sort, append and pop the lowest
    else:
        highest_incomes.append((nome, salario))
        highest_incomes = sorted(highest_incomes, key=lambda x: x[1], reverse=True)
        highest_incomes.pop()


print(highest_incomes[:-1])

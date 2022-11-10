#!/usr/bin/env python
import sys
import csv

# Read each line from stdin
# for line in (sys.stdin.readlines()):
for line in csv.reader(sys.stdin.readlines(), delimiter=","):
    # Get the words in each line
    element = list(line)
    data = (element[0], element[-2][1:])
    salary = data[1]
    name = data[0].split(",")
    if len(name) == 2:
        formated_name = name[1] + " " + name[0]
    else:
        formated_name = name[0]

    print("{0}, {1}\t".format(formated_name, salary))

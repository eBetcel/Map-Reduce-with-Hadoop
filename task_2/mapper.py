#!/usr/bin/env python
import sys
import csv
import re

# Read each line from stdin
# for line in (sys.stdin.readlines()):
for line in csv.reader(sys.stdin.readlines(), delimiter="\t"):
    # Get each line and take names and salary
    element = list(line)

    # ^[A-Z]{1,10}$

    print("{0}, {1}, {2}, {3}, {4}\t".format(element[0], element[1] ,element[2], element[3], element[4]))
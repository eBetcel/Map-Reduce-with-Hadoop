#!/usr/bin/env python
import sys
import csv

# Read each line from stdin
# for line in (sys.stdin.readlines()):
for line in csv.reader(sys.stdin.readlines(), delimiter=','):
  # Get the words in each line
  print(line)

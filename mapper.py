#!/usr/bin/env python
from enum import unique
import sys
import csv
from collections import Counter
# Read each line from stdin
users = []
to_del = ['Logged', 'closed', 'starting', 'in', 'parameters', 'signal']
#names = []
count = 0
log_file = csv.reader(sys.stdin.readlines(), delimiter=' ')
#print(log_file.head())
for line in log_file:
	#print(line[6])
	if line[6] == 'Login:':
		logger_user = line[7].split('=')[-1]
		logger_user = logger_user.split('<')[-1]
		logger_user = logger_user.split('>')[0]
		if logger_user not in to_del:
			#print(logger_user)
			users.append(logger_user)
			count = count + 1
freq = Counter(users)
#print(freq)
for item in freq:
	print(item, freq[item])
#print(users)
"""
for name in users:
	if name not in names:
		names.append(name)
		print(name)
"""


	
	#if count >= 100:
	#if count< 30:
	# print(line)
	#	users = 
	#count = count +1
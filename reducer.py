#!/usr/bin/env python
import sys
curr_word = None
curr_count = 0

for line in sys.stdin:
  word, count = line.split(' ')
  count = int(count)
  if count > 10:
    print ('Usuário: {0} \nQuantidade de acessos:{1}'.format(word, count))

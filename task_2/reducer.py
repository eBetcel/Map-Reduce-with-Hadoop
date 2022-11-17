#!/usr/bin/env python
import sys
import re

from decimal import Decimal

lesser_or_equal_than_5_url = []

for line in sys.stdin:
    # Get the each pair
    line = line.split("\t")
    id, url, date, time, ip = line[0].split(",")

    if re.search("\/[a-zA-Z]{1,5}\.html$", url):
        lesser_or_equal_than_5_url.append((id, url, date, time, ip))

print(lesser_or_equal_than_5_url)

#!/usr/bin/env python
import math
import sys
lines = sys.stdin.readlines()
n = int(lines[0].strip())
s = lines[1].strip()

DIRECT = ['N','E','S','W']
direct = 0
for turn in s:
    if turn == 'R':
        direct += 1
    else:
        direct += -1

direct = direct % 4

print(DIRECT[direct])
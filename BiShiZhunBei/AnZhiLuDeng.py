#!/usr/bin/env python
import sys

def LuDeng(n,s):
    num = 0

    daolu = list(s.strip().split())
    Y_count = 0

    for i in range(0,len(daolu)):
        if  daolu[i] == 'X' :
            if Y_count != 0:
                if Y_count % 3 == 0:
                    num += int(Y_count / 3)
                else:
                    num += int(Y_count / 3) + 1
            Y_count = 0
        elif daolu[i] == '.':
            Y_count += 1
    print(num)


lines = sys.stdin.readlines()
t = int(lines[0].strip())

for i in range(1,t+1):
    if(i%2 ==0):
        continue
    elif not lines[i].strip():
        continue
    else:
        n = int(lines[i].strip())
        s = lines[i+1].strip()
        LuDeng(n,s)
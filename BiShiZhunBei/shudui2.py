#!/usr/bin/env python
line = input()
n = int(line.split(' ')[0])
k = int(line.split(' ')[1])
count = 0
for x in range(1,n+1):
    for y in range(1,n+1):
        if x % y >= k :
            print('(',x,',',y,')')
            count += 1
print(count)
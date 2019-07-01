#!/usr/bin/env python
n, k = map(int, input().split())
count = 0

if k == 0:
    count = n * n
else:
    for y in range(k+1,n+1):
        count += (n // y) * (y - k)
        if n % y >= k:
            count += (n % y) - k + 1

print(count)
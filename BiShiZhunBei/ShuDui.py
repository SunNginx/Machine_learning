#!/usr/bin/env python
n, k = map(int, input().split())
count = 0

if k == 0:
    count = n * n
else:
    for x in range(k, n + 1):
        y = k + 1
        while k < y < x:
            if x % y >= k:
                count += 1
            y += 1
        count += n - x


print(count)
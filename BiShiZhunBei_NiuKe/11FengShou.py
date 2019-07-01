#通过率20%，报错了，但是不知道哪里错了
import sys

def DuiShu(a,left):
    if left - A[a] <= 0 :
        return a+1
    else:
        return DuiShu(a+1,left - A[a])

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    n = int(lines[0])
    A = list(map(int, lines[1].split()))
    m = int(lines[2])
    Q = list(map(int, lines[3].split()))
    for q in Q:
        result = DuiShu(0,q)
        print(result)



#扫了一眼大神的讨论，发现用到二分查找方法，自己想了以下方法
# 运行通过，
# 运行时间：479ms
#占用内存：20084k
#!/usr/bin/env python
#通过率100%

import sys
import bisect
lines = sys.stdin.readlines()
n = int(lines[0])
A = list(map(int,lines[1].split()))
m = int(lines[2])
Q = list(map(int,lines[3].split()))
ADD_A = []
count = 0
for i in range(n):
    count += A[i]
    ADD_A.append(count)
# print(ADD_A)
index = 0
for j in range(m):
    index = bisect.bisect_left(ADD_A,Q[j]) + 1
    print(index)
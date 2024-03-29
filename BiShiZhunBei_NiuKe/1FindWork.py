#!/usr/bin/env python

import sys
import bisect
task = {}
lines = sys.stdin.readlines()
n, m = map(int, lines[0].strip().split())
for line in lines[1:-1]:
    buff1 = line.strip().split()
    if not line.strip().split():
        continue
    a, b = map(int, line.strip().split())
    buff = task.get(a, 0)
    task[a] = max(task.get(a, 0), b)
arr = sorted(task.keys())
print('before:',task)
for i in range(1, len(arr)):
    if task[arr[i]] < task[arr[i -1]]:
        task[arr[i]] = task[arr[i -1]]
print('after:',task)
skills = map(int, lines[-1].strip().split())
for skill in skills:
    if skill in task:
        print(task[skill])
    else:
        ind = bisect.bisect(arr, skill)
        if ind == 0:
            print(0)
        else:
            print(task[arr[ind -1]])
            #update

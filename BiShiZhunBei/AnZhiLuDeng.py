#!/usr/bin/env python

def LuDeng(n, s):
    num = 0
    pos = 0
    while pos < len(s):
        point = s[pos]
        if point == '.':
            num += 1
            pos += 3
        else:
            pos += 1

    print(num)

if __name__ == '__main__':
    count = int(input())
    for i in range(count):
        n = int(input())
        s = input()
        LuDeng(n,s)



#!/usr/bin/env python
#输入一行 多个字符 如 5 3
n, k = map(int, input().split())
#一行多个转换为list
import sys
lines = sys.stdin.readlines()
x1 = list(map(int,lines[1].split()))

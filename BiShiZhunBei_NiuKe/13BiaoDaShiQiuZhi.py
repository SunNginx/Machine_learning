#通过率100%
number = list(map(int,input().split()))
number.sort()
if 1 in number:
    print((number[0]+number[1])*number[2])
else:
    print(number[0]*number[1]*number[2])
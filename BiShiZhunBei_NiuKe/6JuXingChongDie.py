#
import sys

lines = sys.stdin.readlines()
n = int(lines[0].strip())
x1 = list(map(int,lines[1].split()))
y1 = list(map(int,lines[2].split()))
x2 = list(map(int,lines[3].split()))
y2 = list(map(int,lines[4].split()))
COUNT = []
#下面是原来的思路，我是看每一个矩形，与多少其他的矩形交叠，
#但是，本题目的目的是计算出平面内重叠矩形数量最多的地方,有多少个矩形相互重叠。
#这个交叠最多的区域，他不一一定是某一个矩形，因此之前考虑的都是不对的
# X = []
# Y = []
# for i in range(n):
#     count = 0
#     X = list([x1[i],x2[i]])
#     Y = list([y1[i],y2[i]])
#     X.sort()
#     Y.sort()
#     for j in range(n):
#         if x1[j] == X[0] and x2[j] == X[1] and y1[j] == Y[0] and y2[j] == Y[1]:
#             count += 1
#         elif (X[0] < x1[j] < X[1] or X[0] < x2[j] < X[1]) and (Y[0] < y1[j] < Y[1] or Y[0] < y2[j] < Y[1]):
#             count += 1
#     COUNT.append(count)
# print(max(COUNT))

#正确代码如下
# 遍历所有点的组合（包含了矩形所有角以及交点），看一下有多少矩形包含它
res = 1
for x in x1+x2:
    for y in y1+y2:
        cnt = 0
        for i in range(n):
            if x > x1[i] and y > y1[i] and x <= x2[i] and y <= y2[i]:
                cnt += 1
        res = max(res,cnt)
print(res)
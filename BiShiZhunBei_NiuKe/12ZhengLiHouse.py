#自己写的代码
#暴力方法
#通过率100%
#!/usr/bin/env python
import math
#计算两点距离
def TwoPointDistence(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

#平面上四个点是否组成正方形，任意两点的距离，必有四条相等的边和，两条相等的对角线，且边长小于对角线
def IsSquare(x1,y1,x2,y2,x3,y3,x4,y4):
    D = []
    D.append(TwoPointDistence(x1,y1,x2,y2))
    D.append(TwoPointDistence(x1,y1,x3,y3))
    D.append(TwoPointDistence(x1,y1,x4,y4))
    D.append(TwoPointDistence(x2,y2,x3,y3))
    D.append(TwoPointDistence(x3,y3,x4,y4))
    D.append(TwoPointDistence(x2,y2,x4,y4))
    D.sort()

    if D[0] == D[1] == D[2] == D[3] and D[4] == D[5] and D[3] < D[5]:
        return True
    else:
        return False
#（a,b)点 绕（x,y)逆时针旋转90度之后，对应的坐标
def NiShiZheng90(Point,N): #Point = [] :a,b,x,y; N 为旋转次数
    if N > 0 :
        after_a = Point[3] - Point[1] + Point[2]
        after_b = Point[0] - Point[2] + Point[3]
        return after_a, after_b

    return Point[0],Point[1]

#计算每一团物品的最少移动次数
def MinMove(tuan):#tuan = [],包含四个物品的坐标，即[[1, 1, 0, 0], [-1, 1, 0, 0], [-1, 1, 0, 0], [1, -1, 0, 0]]
    move = []
    x1,y1 = map(int,tuan[0][0:2])
    x2,y2 = map(int,tuan[1][0:2])
    x3,y3 = map(int,tuan[2][0:2])
    x4,y4 = map(int,tuan[3][0:2])
    for i in range(4):
        if i == 0:
            x1 = tuan[0][0]
            y1 = tuan[0][1]
        x1, y1 = NiShiZheng90([x1,y1,tuan[0][2],tuan[0][3]],i)
        for j in range(4):
            # print('j=',j)
            if j == 0 :
                x2 = tuan[1][0]
                y2 = tuan[1][1]
            x2, y2 = NiShiZheng90([x2,y2,tuan[1][2],tuan[1][3]],j)
            for k in range(4):
                if k == 0:
                    x3 = tuan[2][0]
                    y3 = tuan[2][1]
                x3, y3 = NiShiZheng90([x3,y3,tuan[2][2],tuan[2][3]],k)
                for l in range(4):
                    # print('l=',l)
                    if l == 0:
                        x4 = tuan[3][0]
                        y4 = tuan[3][1]
                    x4, y4 = NiShiZheng90([x4,y4,tuan[3][2],tuan[3][3]],l)
                    if IsSquare(x1, y1, x2, y2, x3, y3, x4, y4):
                        move.append(i + j + k + l)

    if move:
        minMove = min(move)
        return minMove
    else:
        return -1

def main():
    n = int(input())
    A = {}
    for i in range(n):
        ZWpoint = []
        for j in range(4):
            cur_line = list(map(int,input().split()))
            ZWpoint.append(cur_line)
        A[i] = ZWpoint
    for key,tuan in A.items():
        print(MinMove(tuan))

if __name__ == '__main__':
    main()
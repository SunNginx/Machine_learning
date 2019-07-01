#第一种想法，是先统计出所有的清醒时间的知识点分值
#然后遇到T为0时，统计该次叫醒获得的原睡觉的知识点分值，统计时间在保持时间内
#但是通过率只有70%
# import sys
# def GetKeepWeakUpValue(A,T,k):
#     value = 0
#     for i in range(len(T)) :
#         if T[i] == 0 :
#             value += A[i]
#     return value
#
# if __name__ == '__main__':
#     lines = sys.stdin.readlines()
#     n,k = map(int,lines[0].split())
#     A = list(map(int,lines[1].split()))
#     T = list(map(int,lines[2].split()))
#     WeakUpValue = 0
#     JiaoXingValue = 0
#     for i in range(n):
#         if T[i] == 0:
#             if i+k < len(T):
#                 value = GetKeepWeakUpValue(A[i:i+k],T[i:i+k],k)
#             else:
#                 value = GetKeepWeakUpValue(A[i:],T[i:],k)
#             JiaoXingValue = max(JiaoXingValue,value)
#         else:
#             WeakUpValue += A[i]
#     print(JiaoXingValue+WeakUpValue)
#     print(WeakUpValue)
#     print(JiaoXingValue)

#看了一下别人的思路
#统计清醒时的分值时，可以将清醒时分值置零
#这个代码通过率为90%

# import sys
#
# if __name__ == '__main__':
#     lines = sys.stdin.readlines()
#     n, k = map(int, lines[0].split())
#     A = list(map(int, lines[1].split()))
#     T = list(map(int, lines[2].split()))
#     WeakUpValue = 0
#     JiaoXingValue = 0
#     sleepIndex = []
#     for i in range(n):
#         if T[i] == 1:
#             WeakUpValue += A[i]
#             A[i] = 0
#         else:
#             sleepIndex.append(i)
#
#     for index in sleepIndex:
#         if index + k < n:
#             value = sum(A[index:index + k])
#         else:
#             value = sum(A[index:])
#         JiaoXingValue = max(JiaoXingValue, value)
#     print(JiaoXingValue + WeakUpValue)

#大神的代码
# -*- coding: UTF-8 -*-
#point 所有清醒时间的分数值
#按顺序，计算所有K个时间段内的分数值，取最大值
#大神真厉害
def main():
    a_line = input().split()
    n = int(a_line[0])      #这堂课持续分钟
    k = int(a_line[1])      #叫醒一次清醒时间
    b_line = input().split()    #每分钟知识点兴趣值
    c_line = input().split()    #每分钟是否清醒，1清醒
    cur_ep = 0
    point = 0                   #清醒时知识点兴趣值
    max_ep = 0
    for i in range(n):
        get_p = int(b_line[i])      #当前i 对应的知识点兴趣值
        if c_line[i] == "1":        #如果当前为清醒状态
            point += get_p          #累加所有清醒时间的知识点兴趣值，保存到point
        else:                       #如果当前为睡觉状态
            cur_ep += get_p         #累加睡觉时刻的知识点兴趣值，保存到cur_ep
        if i + 1 > k:               #当当前的时间点，大于保持清醒时间
            #int(b_line[i - k]) 为 这K分钟，的第一分钟的知识点兴趣值
            #if c_line[i - k] == "0" else 0 如果清醒状态，当前为de_ep = 0
            #如果是睡眠状态，de_ep 为这K分钟，的第一分钟的知识点兴趣值
            de_ep = int(b_line[i - k]) if c_line[i - k] == "0" else 0
            cur_ep -= de_ep         #cur_ep 总是只会保存，当前i包括在内的前K个时间的，睡眠时间的知识点分数值
            #因为清醒时刻时，cur_ep 不统计在内。所以cur_ep实际上是，统计了按顺序属的所有K个时长的时刻的分数值，这其中肯定
            #包含睡眠时刻被叫醒的，保持清醒的分数值。
        if cur_ep > max_ep:
            max_ep = cur_ep
    point += max_ep
    print(point)

if __name__ == '__main__':
    main()
# from scipy.special import comb
# from itertools import combinations
#
# n, w = map(int, input().split())
# v = list(map(int, input().split()))
# count = 0
#这是最开始想到的利用外部函数的取组合数求和的方式，但是考试的环境没有外部模块
# if sum(v) <= w:
#     for i in range(1, n+1):
#         print(i,comb(n,i))
#         count += int(comb(n, i))
# else:
#     for i in range(0, n):
#         ZUHEs = list(combinations(v[i], i + 1))
#         for zuhe in ZUHEs:
#             SUM = sum(zuhe)
#             if (SUM <= w):
#                 count += 1
# print(count + 1)

def count_m(n, m, v_list):
    flag = 0
    b = 0
    v_sum = sum(v_list)
    if v_sum < m:
        b = 2 ** (n)
        return b
    else:
        while flag <= n:
            if m - v_list[flag - 1] > 0:
                b += count_m(flag - 1, m - v_list[flag - 1], v_list[:flag])
            flag += 1
    return b+1


n, w = map(int, input().split())
v = list(map(int, input().split()))
print(count_m(len(v), w, sorted(v)))

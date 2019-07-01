# #通过率80%
# import sys
# # lines = sys.stdin.readlines()
# n,k = map(int, input().split())
# A = list(map(int,input().split()))
#
#
# CZ = {}
# Move = []
# if max(A) == min(A) :
#     print(0,0)
# else:
#     for i in range(k):
#         max_a = max(A)
#         min_a = min(A)
#         if max_a != min_a :
#             max_index = A.index(max_a)
#             min_index = A.index(min_a)
#             A[max_index] = max_a - 1
#             A[min_index] = min_a + 1
#             cur_value = max(A) - min(A)
#             if cur_value in CZ:
#                 exist_cishu = CZ[cur_value]
#                 CZ[cur_value] = min(i,exist_cishu)
#             else:
#                 CZ[cur_value] = i
#             Move.append([max_index,min_index])
#         else:
#             CZ[0] = i-1
#             break
#
#     min_value = min(CZ.keys())
#     cishu = int(CZ[min(CZ.keys())])
#     print('cz=',CZ)
#     print(min_value,cishu+1)
#     if Move:
#         for j in range(cishu+1):
#             if j < k:
#                 print(Move[j][0]+1,Move[j][1]+1)

#dasehn
import sys
if __name__ == "__main__":
    lines =  sys.stdin.readlines()
    n,k = list(map(int,lines[0].strip().split(" ")))
    high = list(map(int,lines[1].strip().split(" ")))
    out = []
    numstep = 0
    flag = False
    for i in range(k):
        minh = min(high)
        maxh = max(high)
        if minh == maxh:
            break
        numstep += 1
        indmin = high.index(minh)
        indmax = high.index(maxh)
        high[indmin] += 1
        high[indmax] -= 1
        out.append(str(indmax+1)+" "+str(indmin+1))
    minh = min(high)
    maxh = max(high)
    print(str(maxh-minh)+" "+str(numstep))
    for s in out:
        print(s)
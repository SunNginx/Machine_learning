n, m = map(int, input().split())
c = list(map(int,input().split()))
# print(n)
# print(m)
C = {}
for i in range(1,n+1):
    C[i] = 0
# print(c)
for i in range(m):
    lieshu = c[i]
    # print('temp=',lieshu)
    C[lieshu] += 1

print(min(C.values()))
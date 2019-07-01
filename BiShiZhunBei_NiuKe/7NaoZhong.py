#m没有看答案，做出来的第一题
import sys
import bisect
lines = sys.stdin.readlines()
n = int(lines[0].strip())
NZ = []
for nz in lines[1:n+1]:
    shi = nz.split()[0]
    fen = nz.split()[1]
    time = int(shi)*60+int(fen)
    NZ.append(time)

X = int(lines[n+1])
A = int(lines[n+2].split()[0])*60 + int(lines[n+2].split()[1])

getUpTime = A - X
# print('time get up =',getUpTime)
NZ.sort()
# print('NZ sort =',NZ)
if getUpTime in NZ:
    print(getUpTime // 60, getUpTime % 60)
else:
    should_time = bisect.bisect_left(NZ,getUpTime)-1
    # print('should time=',NZ[should_time])
    print(NZ[should_time]//60,NZ[should_time]%60)

#!/usr/bin/env python
class three:
    def find(self):
        result = []
        temp = input().split()

        for i1 in temp:
            result.append(int(i1))
        left = result[0]
        right = result[1]
        num = int((right - left) / 3)
        ret = num * 2
        right = right - num * 3
        while left <= right:
            if left % 3 != 1:
                ret += 1
            left += 1
        return ret
if __name__ == '__main__':
    a = three()
    print(a.find())

import re
from typing import List
class Solution:

    def solution(self, s:str):

        alpha = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
        steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

        col = int(s[-1])
        row = alpha[s[-2]]
        count = 8

        for step in steps:
            if col+step[0]<1 or col+step[0]>8:
                count-=1
            elif row+step[1]<1 or row+step[1]>8:
                count-=1

        return count

p = Solution()
print(p.solution('a1'))
print(p.solution('c2'))
import re
from typing import List
class Solution:

    def solution(self, n, k):

        count = 0
        while n!=1:
            if n%k==0:
                n/=k
                count+=1
            else:
                n-=1
                count+=1

        return count

p = Solution()
print(p.solution(25,5))
print(p.solution(17,4))
print(p.solution(25,3))
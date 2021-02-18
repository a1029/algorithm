import re
from typing import List

class Solution:

    # 자가풀이여부: X
    def solution(self, n):

        count = 0
        for i in range(n+1):
            for j in range(60):
                for k in range(60):
                    if '3' in str(i)+str(j)+str(k):
                        count += 1

        print(count)

p = Solution()
p.solution(5)
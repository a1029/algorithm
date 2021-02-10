import re
from typing import List
class Solution:

    def solution(self, n, m, arr: List[List[int]]):

        result = []
        for l in arr:
            result.append(min(l))

        return max(result)

p = Solution()
print(p.solution(3,3,[[3,1,2],[4,1,4],[2,2,2]]))
print(p.solution(2,4,[[7,3,1,8],[3,3,3,4]]))
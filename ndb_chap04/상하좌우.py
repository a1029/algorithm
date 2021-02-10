import re
from typing import List
class Solution:

    def solution(self, n, arr: List[str]):

        i,j=1,1
        for d in arr:
            if d=='L':
               if j>=2:
                   j-=1
            elif d=='R':
                if j<=n-1:
                    j+=1
            elif d=='U':
                if i>=2:
                    i-=1
            elif d=='D':
                if i<=n-1:
                    i+=1

        return [i,j]
p = Solution()
print(p.solution(5, ['R','R','R','U','D','D']))
print(p.solution(5, ['D','D','L','R','R','R', 'U', 'L', 'D','D','D']))
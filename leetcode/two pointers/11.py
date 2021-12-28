from typing import List
# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0, n-1
        s = (r-l)*min(height[l],height[r])
        while l < n and r > -1 and l<=r:
            s = max(s, (r-l)*min(height[l],height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return s
        

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1,2,4,3]))
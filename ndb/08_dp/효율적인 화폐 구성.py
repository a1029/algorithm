from typing import List


class Solution:

    # fail
    def solution(self, arr: List[int], m):

        dp = [10000] * (m + 1)
        dp[0] = 0

        for n in arr:
            for i in range(n, m + 1):
                if dp[i - n] != 10000:
                    dp[i] = min(dp[i], dp[i - n] + 1)

        if dp[m] == 10000:
            print(-1)
        else:
            print(dp[m])


p = Solution()
p.solution([2, 3], 15)
p.solution([3, 5, 7], 4)

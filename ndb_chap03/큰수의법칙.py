from typing import List
import collections

class Solution:

    def solution(self, n, m, k, array: List[int]):

        array.sort()
        first = array[-1]
        second = array[-2]
        result = 0
        while True:
            for i in range(k):
                if m==0:
                    break
                result += first
                m-=1
            if m==0:
                break
            result += second
            m-=1
        return result

    def solution2(self, n, m, k, array: List[int]):

        array.sort()
        first = array[-1]
        second = array[-2]
        result = 0

        count = int(m/(k+1))*k + m%(k+1)

        result += count * first
        result += (m-count) * second
        print(count)
        return result

p = Solution()
print(p.solution2(5,8,3,[2,4,5,4,6]))
print(p.solution2(5,7,2,[3,4,3,4,3]))
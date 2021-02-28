from typing import List


class Solution:

    # success
    def my_answer(self, arr: List[int]):
        '''n = int(input())
        array = []
        for i in range(n):
            array.append(int(input()))
        '''

        print(sorted(arr, reverse=True))


p = Solution()
p.my_answer([15, 27, 12])

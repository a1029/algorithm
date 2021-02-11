from typing import List


class Solution:

    # 자가풀이여부: O
    def my_answer(self):
        n = int(input())
        arr = []
        for i in range(n):
            input_data = input().split()
            arr.append((input_data[0], int(input_data[1])))

        arr.sort()

        for name, score in arr:
            print(score, end=' ')


p = Solution()
p.my_answer()

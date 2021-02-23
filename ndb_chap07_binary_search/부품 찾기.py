from typing import List
from collections import Counter


class Solution:

    # success
    def my_answer(self, n, arr1: List[int], m, arr2: List[int]):

        def bst(arr: List[int], target, start, end):

            if start > end:
                return 'No'
            mid = (start + end) // 2

            if arr[mid] < target:
                return bst(arr, target, mid + 1, end)
            elif arr[mid] > target:
                return bst(arr, target, start, mid - 1)
            else:
                return 'Yes'

        arr1.sort()
        arr2.sort()
        result = []

        for i in range(m):
            result.append(bst(arr1, arr2[i], 0, len(arr1)))

        print(' '.join(result))

    def my_answer2(self, n, arr1: List[int], m, arr2: List[int]):

        arr1.sort()
        arr2.sort()
        result = []
        c1 = Counter(arr1)
        for n in arr2:
            if n in c1:
                result.append('yes')
            else:
                result.append('no')

        print(' '.join(result))


p = Solution()
p.my_answer(5, [8, 3, 7, 9, 2], 3, [5, 7, 9])
p.my_answer2(5, [8, 3, 7, 9, 2], 3, [5, 7, 9])

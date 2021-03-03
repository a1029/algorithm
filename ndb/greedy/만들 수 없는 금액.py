from typing import List


# X
def solution(n, arr: List[int]):
    arr.sort()
    target = 1
    for n in arr:
        if target < n:
            print(target)
            break
        target += n


solution(5, [3, 2, 1, 1, 9])  # 8
solution(3, [3, 5, 7])  # 1
solution(3, [1, 2, 3, 8])  # 7
solution(5, [1, 2, 4, 8, 17])  # 16
solution(4, [1, 2, 4, 9])  # 8

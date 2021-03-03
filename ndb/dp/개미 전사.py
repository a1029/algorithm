from typing import List

# X
def solution(arr: List[int]):
    d = [0] * len(arr)
    d[0] = arr[0]
    d[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        d[i] = max(d[i - 1], d[i - 2] + arr[i])

    print(max(d))

solution([1, 3, 1, 5])

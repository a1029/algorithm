from typing import List


# O
def my_answer(m, arr: List[int]):

    arr2 = [0] * len(arr)

    for i in range(max(arr), -1, -1):
        for j in range(len(arr)):
            arr2[j] = arr[j] - i
            if arr2[j] < 0:
                arr2[j] = 0
        if sum(arr2) >= m:
            print(i)
            return

def solution(m, arr: List[int]):

    start, end = 0, max(arr)
    result = 0
    while start < end:

        mid = (start + end) // 2
        total = sum([x - mid for x in arr if x > mid])
        if m > total:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    print(result)


my_answer(6, [19, 15, 10, 17])
solution(6, [19, 15, 10, 17])

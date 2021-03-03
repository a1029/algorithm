from typing import List
import itertools
import collections


# X
def my_answer(data: List[int]):
    counter = collections.Counter(data)
    counter = sorted(counter.items())
    n = len(data)
    result = 0
    for k, v in counter:
        result += v * (n - v)
        n -= v
    print(result)


def solution(data):
    n = len(data)
    m = max(data)
    array = [0] * 11
    for x in data:
        array[x] += 1
    result = 0
    for i in range(1, m + 1):
        n -= array[i]
        result += array[i] * n

    print(result)


my_answer([1, 3, 2, 3, 2]) # 8
my_answer([1, 5, 4, 3, 2, 4, 5, 2]) # 25
my_answer([1, 3, 2, 5, 6, 4, 3, 2, 2, 1]) # 40
solution([1, 3, 2, 3, 2])
solution([1, 5, 4, 3, 2, 4, 5, 2])
solution([1, 3, 2, 5, 6, 4, 3, 2, 2, 1])


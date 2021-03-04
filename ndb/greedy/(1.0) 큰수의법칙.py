from typing import List
import collections

# O
def my_answer(n, m, k, array: List[int]):

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

    print(result)


def solution(n, m, k, array: List[int]):

    array.sort()
    first = array[-1]
    second = array[-2]
    result = 0

    count = int(m/(k+1))*k + m%(k+1)

    result += count * first
    result += (m-count) * second

    print(result)


my_answer(5,8,3,[2,4,5,4,6])
solution(5,8,3,[2,4,5,4,6])
my_answer(5,7,2,[3,4,3,4,3])
solution(5,7,2,[3,4,3,4,3])
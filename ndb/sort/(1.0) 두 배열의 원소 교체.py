from typing import List


# O
def my_answer(arr1: List[int], arr2: List[int], k):

    arr1.sort()
    arr2.sort()

    for i in range(k):
        arr1[i] = arr2[-i]

    print(sum(arr1))

def solution(arr1: List[int], arr2: List[int], k):

    arr1.sort()
    arr2.sort(reverse=True)

    for i in range(k):
        if arr1[i] < arr2[i]:
            arr1[i], arr2[i] = arr2[i], arr1[i]
        else:
            break
    print(sum(arr1))


my_answer([1, 2, 5, 4, 3], [5, 5, 6, 6, 5], 3)
solution([1, 2, 5, 4, 3], [5, 5, 6, 6, 5], 3)

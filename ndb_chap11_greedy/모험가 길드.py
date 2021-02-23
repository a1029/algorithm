from typing import List

# fail
def my_answer(n, arr: List[int]):

    arr.sort()
    count = 0
    result = 0
    for x in arr:
        count += 1
        if count >= x:
            result += 1
            count = 0

    print(result)

def solution(n, arr: List[int]):
    count = 0
    result = 0
    arr.sort()

    for i in arr:
        count += 1
        if count>=i:
            result += 1
            count = 0
    print(result)

my_answer(5, [2,3,1,2,2])
my_answer(10, [5])
my_answer(10, [10,1,1,1,1,1,1,1,1,1])
solution(5, [2,3,1,2,2])
solution(10, [5])
solution(10, [10,1,1,1,1,1,1,1,1,1])
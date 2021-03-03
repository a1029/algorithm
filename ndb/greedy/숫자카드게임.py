
from typing import List

# O
def my_answer(n, m, arr: List[List[int]]):

    result = []
    for l in arr:
        result.append(min(l))

    print(max(result))


my_answer(3,3,[[3,1,2],[4,1,4],[2,2,2]])
my_answer(2,4,[[7,3,1,8],[3,3,3,4]])
import math
from itertools import permutations

def solution(numbers):
    answer = set()
    n = len(numbers)
    for case in permutations(numbers, len(numbers)):
        arr = set()
        for i in range(1, 2**n):
            tmp = ""
            for j in range(n):
                if i & (1 << j):
                    tmp += list(case)[j]
            arr.add(int(tmp))
        for num in arr:
            flag = True
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    flag = False
                    break
            if flag and num >= 2:
                answer.add(num)
    return len(answer)

def solution2(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
print(solution("17"))
print(solution("011"))
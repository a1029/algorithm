from itertools import combinations
import math

def get_subsequences(arr, n):
    opsize = math.pow(2, n)
    result = []
    for counter in range(1, int(opsize)):
        tmp = []
        for j in range(0, n):
            if counter & (1<<j):
                tmp.append(arr[j])
        result.append(tmp)
    return result
    
tc = int(input())
for _ in range(tc):
    b = list(map(int, input().split()))
    for combi in combinations(b, 3):
        subsequences = get_subsequences(combi, 3)
        sums = list(map(lambda x: sum(x), subsequences))
        if b == sorted(sums):
            print(' '.join(list(map(str, combi))))
            break


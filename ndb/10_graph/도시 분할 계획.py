from typing import List

# success
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):

    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def my_answer(n,m,paths: List[List[int]]):

    parent = [0] * (n + 1)
    total_cost = 0
    max_cost = 0
    result = []

    for i in range(1, n + 1):
        parent[i] = i

    paths.sort(key=lambda x: x[2])

    for a,b,c in paths:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result.append((a,b))
            total_cost += c
            max_cost = c

    print(result, total_cost, total_cost-max_cost)


my_answer(7,12,[[1,2,3],
                [1,3,2],
                [3,2,1],
                [2,5,2],
                [3,4,4],
                [7,3,6],
                [5,1,5],
                [1,6,2],
                [6,4,1],
                [6,5,3],
                [4,5,3],
                [6,7,4]])
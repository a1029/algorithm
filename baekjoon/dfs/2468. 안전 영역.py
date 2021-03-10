import sys
from copy import deepcopy

# O
sys.setrecursionlimit(100000)

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

max_height = 0
for i in range(n):
    for j in range(n):
        max_height = max(max_height, data[i][j])


def dfs(i, j, t):
    if i < 0 or i >= n or j < 0 or j >= n or t[i][j] <= 0:
        return

    t[i][j] = 0
    dfs(i, j + 1, t)
    dfs(i, j - 1, t)
    dfs(i + 1, j, t)
    dfs(i - 1, j, t)


def rain(t, height):
    for i in range(n):
        for j in range(n):
            t[i][j] -= height


result = 0

for h in range(0, max_height + 1):
    temp = deepcopy(data)
    rain(temp, h)
    area = 0
    for i in range(n):
        for j in range(n):
            if temp[i][j] > 0:
                dfs(i, j, temp)
                area += 1

    result = max(result, area)

print(result)
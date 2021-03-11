import sys

sys.setrecursionlimit(200000)

n = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n + 1)]
array = [[] for _ in range(n + 1)]

array[1] = ['S', 0]
for i in range(2, n + 1):
    a, b, c = sys.stdin.readline().strip().split()
    graph[int(c)].append(i)
    array[i] = [a, int(b)]


def dfs(v):
    if not graph[v]:
        if array[v][0] == 'S':
            return array[v][1]
        else:
            return 0

    if array[v][0] == 'S':
        for w in graph[v]:
            array[v][1] += dfs(w)
        return array[v][1]
    else:
        for w in graph[v]:
            array[v][1] -= dfs(w)
        if array[v][1] < 0:
            return -array[v][1]
        else:
            return 0


print(dfs(1))

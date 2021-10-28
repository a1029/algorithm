import sys

sys.setrecursionlimit(200000)

n = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n + 1)]
String = [[] for _ in range(n + 1)]

String[1] = ['S', 0]
for i in range(2, n + 1):
    a, b, c = sys.stdin.readline().strip().split()
    graph[int(c)].append(i)
    String[i] = [a, int(b)]


def dfs(v):
    if not graph[v]:
        if String[v][0] == 'S':
            return String[v][1]
        else:
            return 0

    if String[v][0] == 'S':
        for w in graph[v]:
            String[v][1] += dfs(w)
        return String[v][1]
    else:
        for w in graph[v]:
            String[v][1] -= dfs(w)
        if String[v][1] < 0:
            return -String[v][1]
        else:
            return 0


print(dfs(1))

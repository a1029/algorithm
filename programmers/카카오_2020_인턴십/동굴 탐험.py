from collections import defaultdict
from collections import deque
import sys
sys.setrecursionlimit(10**6)

graph = defaultdict(list)
tree = defaultdict(list)

def is_cycle(node, visit, recur):

    if visit[node]:
        return True
    if recur[node]:
        return False
    visit[node] = True
    recur[node] = True

    for parent in tree[node]:
        if is_cycle(parent, visit, recur):
            return True
    visit[node] = False
    return False

def solution(n, path, order):

    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    q = deque([0])
    visit = [False]*n
    visit[0] = True
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not visit[nxt]:
                visit[nxt] = True
                tree[nxt].append(now)
                q.append(nxt)

    for a, b in order:
        tree[b].append(a)

    visit = [False]*n
    recur = [False]*n   # 경로 압축 변수 (시간 단축용)
    for node in range(n):
        if is_cycle(node, visit, recur):
            return False
    return True

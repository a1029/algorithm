from collections import deque
def solution(n, computers):
    answer = 0
    visit = [False]*(n)
    for i in range(n):
        if visit[i]:
            continue
        q = deque([i])
        while q:
            v = q.popleft()
            for nv, c in enumerate(computers[v]):
                if c == 1 and not visit[nv]:
                    visit[nv] = True
                    q.append(nv)
        answer += 1
    return answer



def dfs(v, graph, visit):
    visit[v] = True
    for nv, c in enumerate(graph[v]):
        if c == 1 and not visit[nv]:
            dfs(nv, graph, visit)

def solution2(n, computers):
    answer = 0
    visit = [False]*(n)
    for i in range(n):
        if not visit[i]:
            dfs(i, computers, visit)
            answer += 1
    return answer

#print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
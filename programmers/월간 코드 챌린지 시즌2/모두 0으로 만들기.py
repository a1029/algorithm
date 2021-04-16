import collections

def check(a):
    return True if sum(a)==0 else False

def solution(a, edges):
    tree = [[] for _ in range(len(a))]
    indegree = [0]*(len(a))
    visited = [False]*len(a)
    answer = 0
    for i,j in edges:
        tree[i].append(j)
        tree[j].append(i)
        indegree[i] += 1
        indegree[j] += 1

    leaf = collections.deque()
    for i in range(len(indegree)):
        if indegree[i]==1:
            leaf.append(i)

    while leaf:
        now = leaf.popleft()
        visited[now] = True
        for nxt in tree[now]:
            if not visited[nxt]:
                tmp = a[now]
                a[now] -= tmp
                a[nxt] += tmp
                answer += abs(tmp)
                indegree[nxt] -= 1
                if indegree[nxt]==1:
                    leaf.append(nxt)

    return answer if check(a) else -1
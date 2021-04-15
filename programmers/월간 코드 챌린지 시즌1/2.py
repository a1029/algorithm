
def check(a):
    if sum(a)==0:
        return True
    return False

def solution(a, edges):
    tree = [[] for _ in range(len(a))]
    indegree = [0]*(len(a))
    for i,j in edges:
        tree[i].append(j)
        tree[j].append(i)
        indegree[i] += 1
        indegree[j] += 1

    leaf = []
    for i in range(len(indegree)):
        if indegree[i]==1:
            leaf.append(i)
    visit = []
    res = 0
    while leaf:
        now = leaf.pop(0)
        visit.append(now)
        for nxt in tree[now]:
            if nxt not in visit:
                t = a[now]
                a[now] -= t
                a[nxt] += t
                res += abs(t)
                indegree[nxt] -= 1
                if indegree[nxt]==1:
                    leaf.append(nxt)
    if check(a):
        return res
    else:
        return -1

print(solution([-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]]))
print(solution([0,1,0],[[0,1],[1,2]]))
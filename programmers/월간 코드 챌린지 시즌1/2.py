
def check(a):
    if sum(a)==0:
        return True
    return False

def solution(a, edges):
    tree = [[] for _ in range(len(a))]
    for i,j in edges:
        tree[i].append(j)
        tree[j].append(i)
    roots = []
    for i,j in enumerate(tree):
        if len(j)==1:
            roots.append(i)

    for r in roots:
        q = [r]
        visit = [r]
        res = 0
        while q:
            now = q.pop(0)
            for nxt in tree[now]:
                if nxt not in visit:
                    if a[now]==0:
                        t = a[nxt]
                        a[now] += t
                        a[nxt] -= t
                        res += abs(t)
                    else:
                        t = a[now]
                        a[now] -= t
                        a[nxt] += t
                        res += abs(t)
                    q.append(nxt)
                    visit.append(nxt)
        print(res)

print(solution([-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]]))
#print(solution([0,1,0],[[0,1],[1,2]]))
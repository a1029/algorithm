from collections import defaultdict, deque

answer = 1
n = 0
visit = [False]*(1<<17)
def solution(info, edges):
    global answer, n, visit
    n = len(info)
    tree = defaultdict(list)
    for a,b in edges:
        tree[a].append(b)
    queue(1, info, tree)
    return answer

def recursion(state, info, tree):
    global answer, n, visit
    
    if visit[state]:
        return
    visit[state] = True
    
    total, wolf = 0, 0
    for i in range(n):
        if state & (1<<i):
            total += 1
            wolf += info[i]
    
    if wolf*2 >= total:
        return
    answer = max(answer, total-wolf)
    
    for i in range(n):
        if not (state & (1<<i)):
            continue
        for nxt in tree[i]:
            recursion(state | (1<<nxt), info, tree)


def queue(state, info, tree):
    global n, answer, visit
    q = deque([1])
    visit = [False]*(1<<17)
    while q:
        state = q.popleft()
        total, wolf = 0,0 
        for i in range(n):
            if state & (1<<i):
                total += 1
                wolf += info[i]
        if wolf*2 >= total:
            continue
        answer = max(answer, total-wolf)
        for i in range(n):
            if not (state & (1<<i)):
                continue
            for nxt in tree[i]:
                if not visit[state|(1<<nxt)]:
                    q.append(state|(1<<nxt))
                    visit[state|(1<<nxt)] = True
    return answer
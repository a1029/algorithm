from collections import defaultdict, deque

n, k = map(int, input().split())
count = defaultdict(int)
answer = int(1e9)
q = deque([[n, 0]])
visit = [False]*100001

if n > k:
    print(n-k)
    print(1)
    exit()

while q:
    now, time = q.popleft()
    visit[now] = True
    if now==k:
        answer = min(answer, time)
        count[time] += 1
    else:
        if 0 <= now-1 and not visit[now-1]:
            q.append([now-1, time+1])
        if now+1 <= 100000 and not visit[now+1]:
            q.append([now+1, time+1])
        if now*2 <= 100000 and not visit[now*2]:
            q.append([now*2, time+1])

print(answer)
print(count[answer])

# 5 6 12 18 17
from collections import deque

cony, brown = 11, 2
q = deque([brown])
visit = [False for _ in range(200001)]
time = 1
answer = 0
while True:
    if cony > 200000:
        print(-1)
        break
    cony += time
    for _ in range(len(q)):
        now = q.popleft()
        b_plus = now + 1
        b_minus = now - 1
        b_times = now * 2

        if b_plus == cony or b_minus == cony or b_times == cony:
            print(time)
            exit()
        else:
            q.append(b_plus)
            q.append(b_minus)
            q.append(b_times)
    time += 1

'''time = 0
cony, brown = 11, 2
q = deque([[brown, 0]])
visit = [[False]*2 for _ in range(200001)]
while True:
    cony += time
    if cony > 200000:
        print(-1)
        break
    if visit[cony][time%2]:
        print(time)
        break
    
    for i in range(len(q)):
        now, t = q.popleft()
        new_t = (t+1)%2

        if 0 <= now-1 and not visit[now-1][new_t]:
            visit[now-1][new_t] = True
            q.append([now-1, new_t])
        if now+1 < 200001 and not visit[now+1][new_t]:
            visit[now+1][new_t] = True
            q.append([now+1, new_t])
        if now*2 < 200001 and not visit[now*2][new_t]:
            visit[now*2][new_t] = True
            q.append([now*2, new_t])
    time += 1'''

# input: 11 2
# answer: 5
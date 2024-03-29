import itertools
import copy
import collections
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
virus = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
answer = int(1e9)
answer2 = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            arr[i][j] = 0
            virus.append([i,j])
for case in itertools.combinations(virus, m):
    tmp = copy.deepcopy(arr)
    q = collections.deque()
    count = 0
    for x,y in case:
        tmp[x][y] = 2
        q.append([x,y])
    while q:
        for _ in range(len(q)):
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if tmp[nx][ny]==0:
                        tmp[nx][ny] = 2
                        q.append([nx,ny])
        if len(q):
            count += 1
    if any(0 in tmp[i] for i in range(n)):
        answer2 += 1
    else:
        answer = min(answer, count)
if answer2 == len(list(itertools.combinations(virus, m))):
    print(-1)
else:
    print(answer)

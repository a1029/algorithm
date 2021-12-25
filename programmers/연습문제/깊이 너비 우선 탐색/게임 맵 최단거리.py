from collections import deque

# https://programmers.co.kr/learn/courses/30/lessons/1844
def solution(maps):
    answer = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    n = len(maps)
    m = len(maps[0])
    visit = [[False]*m for _ in range(n)]
    dist = [[0]*m for _ in range(n)]
    visit[0][0] = True
    dist[0][0] = 1
    q = deque()
    start = [0,0,dist[0][0]]
    q.append(start)
    while q:
        x,y,d = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and maps[nx][ny] == 1:
                q.append([nx,ny,d+1])
                visit[nx][ny] = True
                dist[nx][ny] = d+1

    if dist[n-1][m-1] == 0:
        return -1
    else:
        return dist[n-1][m-1]

    return answer
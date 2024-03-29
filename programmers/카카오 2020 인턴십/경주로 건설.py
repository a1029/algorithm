from collections import deque


def solution(board):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    n = len(board)

    def bfs(start):
        q = deque([start])
        dist = [[1e9] * n for _ in range(n)]
        dist[0][0] = 0
        while q:
            x,y,c,d = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                nc = c + 100 if d==i else c + 600
                if 0<=nx<n and 0<=ny<n and board[nx][ny]==0 and nc<dist[nx][ny]:
                    dist[nx][ny] = nc
                    q.append((nx,ny,nc,i))
        return dist[n-1][n-1]

    return min(bfs((0,0,0,0)), bfs((0,0,0,1)))
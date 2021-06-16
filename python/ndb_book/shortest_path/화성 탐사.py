import heapq

for _ in range(int(input())):
    n = int(input())
    inf = int(1e9)
    dist = [[inf]*n for _ in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    dist[0][0] = graph[0][0]
    q = []
    heapq.heappush(q, (dist[0][0],0,0))
    while q:
        d,x,y = heapq.heappop(q)
        if dist[x][y] < d:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                cost = dist[x][y] + graph[nx][ny]
                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost
                    heapq.heappush(q, (dist[nx][ny],nx,ny))
    print(dist[n-1][n-1])

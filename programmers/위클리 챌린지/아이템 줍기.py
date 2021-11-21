def solution(rectangle, characterX, characterY, itemX, itemY):

    start_x = characterX * 2
    start_y = characterY * 2
    end_x = itemX * 2
    end_y = itemY * 2
    visit = [[False]*101 for _ in range(101)]
    graph = [[0]*101 for _ in range(101)]

    for x1,y1,x2,y2 in rectangle:
        for i in range(x1*2, x2*2+1):
            for j in range(y1*2, y2*2+1):
                graph[i][j] = 1

    for x1,y1,x2,y2 in rectangle:
        for i in range(x1*2+1, x2*2):
            for j in range(y1*2+1, y2*2):
                graph[i][j] = 0

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    q = []
    start = [start_x, start_y, 0]
    visit[start_x][start_y] = True
    q.append(start)
    while q:
        x,y,c = q.pop(0)
        if(x==end_x and y==end_y):
            return c/2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx<0 or ny<0 or nx > 100 or ny>100):
                continue
            if(graph[nx][ny]==1 and not visit[nx][ny]):
                q.append([nx,ny,c+1])
                visit[nx][ny] = True

import collections

def get_next_pos(pos, new_board):

    next_pos = []
    pos = list(pos)
    x1,y1,x2,y2 = pos[0][0],pos[0][1],pos[1][0],pos[1][1]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx1,ny1,nx2,ny2 = x1+dx[i],y1+dy[i],x2+dx[i],y2+dy[i]
        if new_board[nx1][ny1]==0 and new_board[nx2][ny2]==0:
            next_pos.append({(nx1,ny1),(nx2,ny2)})
    if x1==x2:
        for i in [-1,1]:
            if new_board[x1+i][y1]==new_board[x2+i][y2]==0:
                next_pos.append({(x1,y1),(x1+i,y1)})
                next_pos.append({(x2,y2),(x2+i,y2)})
    if y1==y2:
        for i in [-1,1]:
            if new_board[x1][y1+i]==new_board[x2][y2+i]==0:
                next_pos.append({(x1,y1),(x1,y1+i)})
                next_pos.append({(x2,y2),(x2,y2+i)})
    return next_pos


def solution(board):
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    pos = {(1,1),(1,2)}
    visit = []
    q = collections.deque()
    q.append((pos,0))
    visit.append(pos)

    while q:
        pos,time = q.popleft()
        if (n,n) in pos:
            return time
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visit:
                visit.append(next_pos)
                q.append((next_pos, time+1))

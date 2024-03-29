def solution(game_board, table):

    board_block = get_block(game_board, 0)
    table_block = get_block(table, 1)

    board_squares = make_square(board_block)
    table_squares = make_square(table_block)

    filled = []

    for square in table_squares:
        rotated = square
        for _ in range(4):
            rotated = rotate_square(rotated)
            if(rotated in board_squares):
                board_squares.pop(board_squares.index(rotated))
                filled.append(rotated)
                break

    answer = 0
    for square in filled:
        for row in square:
            answer += row.count(1)
    return answer

def get_block(graph, a):

    poses = []
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    n = len(graph)
    m = len(graph[0])
    visit = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j]==a and not visit[i][j]:
                q = [[i,j]]
                tmp = [[i,j]]
                visit[i][j] = 1
                while q:
                    x,y = q.pop(0)
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==a and not visit[nx][ny]:
                            q.append([nx,ny])
                            tmp.append([nx,ny])
                            visit[nx][ny] = 1
                poses.append(tmp)
                
    return poses

def make_square(blocks):

    squares = []

    for block in blocks:
        min_x, min_y, max_x, max_y = 51, 51, -1, -1
        for x,y in block:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y ,y)
        square = [[0]*(max_y-min_y+1) for _ in range(max_x-min_x+1)]
        for x,y in block:
            square[max_x-x][max_y-y] = 1
        squares.append(square)

    return squares


def rotate_square(square):

    n = len(square)
    m = len(square[0])
    result = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = square[i][j]

    return result

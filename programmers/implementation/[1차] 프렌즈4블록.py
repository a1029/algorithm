
def solution(m, n, board):

    board = [list(x) for x in board]
    while True:
        remove = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != '#':
                    remove.add((i,j))
                    remove.add((i+1,j))
                    remove.add((i,j+1))
                    remove.add((i+1,j+1))
        if not remove:
            break
        for i,j in remove:
            board[i][j] = '#'
        for _ in range(m):
            for i in range(m-1):
                for j in range(n):
                    if board[i+1][j]=='#':
                        board[i][j],board[i+1][j] = board[i+1][j],board[i][j]

    answer = sum(x.count('#') for x in board)
    return answer

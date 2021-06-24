
n = int(input())
board = [list(input()) for _ in range(n)]
result = 0

def cal():
    global result
    for i in range(n):
        row = 1
        col = 1
        for j in range(n-1):
            if board[i][j]==board[i][j+1]:
                row += 1
            else:
                result = max(result, row)
                row = 1
            if board[j][i]==board[j+1][i]:
                col += 1
            else:
                result = max(result ,col)
                col = 1
        result = max(result, row, col)

for i in range(n):
    for j in range(n-1):
        if board[i][j] != board[i][j+1]:
            board[i][j],board[i][j+1] = board[i][j+1],board[i][j]
            cal()
            board[i][j],board[i][j+1] = board[i][j+1],board[i][j]
        if board[j][i] != board[j+1][i]:
            board[j][i],board[j+1][i] = board[j+1][i],board[j][i]
            cal()
            board[j][i],board[j+1][i] = board[j+1][i],board[j][i]

print(result)


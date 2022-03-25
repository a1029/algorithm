def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])

    newboard = [[0]*(m+1) for _ in range(n+1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 2:
            degree = -degree
        
        newboard[r1][c1] -= degree
        newboard[r2+1][c1] += degree
        newboard[r1][c2+1] += degree
        newboard[r2+1][c2+1] -= degree

    for i in range(n+1):
        for j in range(1,m+1):
            newboard[i][j] += newboard[i][j-1]

    for j in range(m):
        for i in range(1, n+1):
            newboard[i][j] += newboard[i-1][j]

    for i in range(n):
        for j in range(m):
            if board[i][j] + newboard[i][j] > 0:
                answer += 1
    return answer


solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])
solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])
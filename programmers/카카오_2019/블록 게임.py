

def check_shape(board,i,j):
    n = len(board)
    if i+1<n and j+2<n and board[i][j]==board[i+1][j]==board[i+1][j+1]==board[i+1][j+2] and board[i][j+1]==board[i][j+2]==0:
        return 1
    elif i+2<n and j+1<n and board[i][j]==board[i+1][j]==board[i+2][j]==board[i+2][j+1] and board[i][j+1]==board[i+1][j+1]==0:
        return 2
    elif i+2<n and j-1>-1 and board[i][j]==board[i+1][j]==board[i+2][j-1]==board[i+2][j] and board[i][j-1]==board[i+1][j-1]==0:
         return 3
    elif i+1<n and j-2>-1 and board[i][j]==board[i+1][j-2]==board[i+1][j-1]==board[i+1][j] and board[i][j-2]==board[i][j-1]==0:
        return 4
    elif i+1<n and j-1>-1 and j+1<n and board[i][j]==board[i+1][j-1]==board[i+1][j]==board[i+1][j+1] and board[i][j-1]==board[i][j+1]==0:
        return 5
    else:
        return 0


def check_install(board,i,j,shape):
    if shape==1:
        for y in range(j, j+3):
            for x in range(i-1, -1, -1):
                if board[x][y]!=0:
                    return False
    elif shape==2:
        for y in range(j, j+2):
            for x in range(i-1, -1, -1):
                if board[x][y]!=0:
                    return False
    elif shape==3:
        for y in range(j-1, j+1):
            for x in range(i-1, -1, -1):
                if board[x][y]!=0:
                    return False
    elif shape==4:
        for y in range(j-2, j+1):
            for x in range(i-1, -1, -1):
                if board[x][y]!=0:
                    return False
    elif shape==5:
        for y in range(j-1, j+2):
            for x in range(i-1, -1, -1):
                if board[x][y]!=0:
                    return False
    return True


def solution(board):

    n = len(board)
    flag = 0
    answer = 0
    while flag!=1:
        flag = 1
        for i in range(n):
            for j in range(n):
                if board[i][j]!=0:
                    if check_shape(board,i,j)==1:
                        if check_install(board,i,j,1):
                            answer+=1
                            flag = 0
                            board[i][j]=board[i][j+1]=board[i][j+2]=board[i+1][j]=board[i+1][j+1]=board[i+1][j+2]=0
                    elif check_shape(board,i,j)==2:
                        if check_install(board,i,j,2):
                            answer+=1
                            flag=0
                            board[i][j]=board[i][j+1]=board[i+1][j]=board[i+1][j+1]=board[i+2][j]=board[i+2][j+1]=0
                    elif check_shape(board,i,j)==3:
                        if check_install(board,i,j,3):
                            answer+=1
                            flag=0
                            board[i][j-1]=board[i][j]=board[i+1][j-1]=board[i+1][j]=board[i+2][j-1]=board[i+2][j]=0
                    elif check_shape(board,i,j)==4:
                        if check_install(board,i,j,4):
                            answer+=1
                            flag=0
                            board[i][j-2]=board[i][j-1]=board[i][j]=board[i+1][j-2]=board[i+1][j-1]=board[i+1][j]=0
                    elif check_shape(board,i,j)==5:
                        if check_install(board,i,j,5):
                            answer+=1
                            flag=0
                            board[i][j-1]=board[i][j]=board[i][j+1]=board[i+1][j-1]=board[i+1][j]=board[i+1][j+1]=0

    return answer

solution([[0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,4,0,0,0],
          [0,0,0,0,0,4,4,0,0,0],
          [0,0,0,0,3,0,4,0,0,0],
          [0,0,0,2,3,0,0,0,5,5],
          [1,2,2,2,3,3,0,0,0,5],
          [1,1,1,0,0,0,0,0,0,5]])

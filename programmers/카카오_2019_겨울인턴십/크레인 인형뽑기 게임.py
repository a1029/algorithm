
def solution(board, moves):

    answer = 0
    basket = []
    for j in moves:
        for i in range(len(board)):
            if board[i][j-1]!=0:
                basket.append(board[i][j-1])
                board[i][j-1] = 0
                break
        if len(basket)>=2 and basket[-1]==basket[-2]:
            answer+=2
            basket.pop()
            basket.pop()
    return answer

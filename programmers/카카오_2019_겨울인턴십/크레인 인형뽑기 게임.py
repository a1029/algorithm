
def solution(board, moves):

    answer = 0
    n = len(board)
    basket = []
    for m in moves:
        for i in range(n):
            if board[i][m-1]!=0:
                basket.append(board[i][m-1])
                board[i][m-1] = 0
                break
        if len(basket)>=2 and basket[-1]==basket[-2]:
            basket.pop()
            basket.pop()
            answer += 2
    return answer
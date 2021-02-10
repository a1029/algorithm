from typing import List
class Solution:

    def solution(self, m, n, board:List[str]):

        board = [list(x) for x in board]

        matched = True
        while matched:
            # 매치 블록 찾기
            matched = []
            for i in range(m-1):
                for j in range(n-1):
                    if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '#':
                        matched.append([i,j])

            # 블록 제거
            for i, j in matched:
                board[i][j] = board[i][j+1] = board[i+1][j] = board[i+1][j+1] = '#'

            # 블록 떨어뜨리기
            for _ in range(m):
                for i in range(m-1):
                    for j in range(n):
                        if board[i+1][j] == '#':
                            board[i][j],board[i+1][j] = '#',board[i][j]

        print(sum(x.count("#") for x in board))

p = Solution()
p.solution(4,5,["CCBDE","AAADE","AAABF","CCBBF"])
p.solution(6,6,["TTTANT","RRFACC","RRRFCC","TRRRAA","TTMMMF","TMMTTJ"])
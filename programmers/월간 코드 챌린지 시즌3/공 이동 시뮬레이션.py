def solution(n, m, x, y, queries):
    answer = -1
    x1,y1 = x,y
    x2,y2 = x,y
    for command,dx in queries[::-1]:
        if command==0:
            if y1 != 0: y1 += dx
            y2 = y2 + dx if y2 + dx < m-1 else m-1
        elif command==1:
            if y2 != m-1: y2 -= dx
            y1 = y1 - dx if y1 - dx > 0 else 0
        elif command==2:
            if x1 != 0: x1 += dx
            x2 = x2 + dx if x2 + dx <= n-1 else n-1
        else:
            if x2 != n-1: x2 -= dx
            x1 = x1 - dx if x1 - dx > 0 else 0

        if y1 > m-1 or y2 < 0 or x1 > n-1 or x2 < 0:
            return 0
            
    answer = (x2-x1+1) * (y2-y1+1)
    return answer


print(solution(2,2,0,0,[[2,1],[0,1],[1,1],[0,1],[2,1]]))
print(solution(2,5,0,1,[[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))

def solution(routes):
    answer = 0
    routes.sort()
    last = routes[0][1]
    for i in range(1, len(routes)):
        if last >= routes[i][0]:
            last = min(last ,routes[i][1])
        else:
            answer += 1
            last = routes[i][1]
    return answer + 1
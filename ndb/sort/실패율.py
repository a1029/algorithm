
def solution(N, stages):

    stages.sort()
    length = len(stages)
    result = []
    for i in range(1,N+1):
        if length<=0:
            result.append([0, i])
            continue
        result.append([stages.count(i)/length, i])
        length -= stages.count(i)
    result.sort(key=lambda x:(-x[0],x[1]))

    answer = [i[1] for i in result]
    return answer
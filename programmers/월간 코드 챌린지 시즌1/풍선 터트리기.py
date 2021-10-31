
def solution(a):

    left = right = 1e9
    maps = [[0]*len(a) for _ in range(2)]

    for i in range(len(a)):
        if left > a[i]:
            left = a[i]
        maps[0][i] = left
        if right > a[len(a)-1-i]:
            right = a[len(a)-1-i]
        maps[1][i] = right

    answer = 0
    for i in range(len(a)):
        if a[i]<=maps[0][i] or a[i]<=maps[1][len(a)-1-i]:
            answer+=1
    return answer
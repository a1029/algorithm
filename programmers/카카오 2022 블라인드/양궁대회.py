from itertools import combinations_with_replacement

answer = []
maxv = -1
def solution(n, info):
    global answer
    rion = [0]*11
    dfs(n, 0, 0, info, rion)
    if not answer:
        return [-1]
    else:
        tmp = [x[::-1] for x in answer]
        return sorted(tmp)[-1][::-1]
        
def dfs(n, count, idx, info, rion):
    global answer, maxv
    if count==n:
        a,b = 0,0
        for i in range(11):
            if info[i] != 0 or rion[i] != 0:
                if info[i] >= rion[i]:
                    a += 10-i
                else:
                    b += 10-i
        if b-a<=0:
            return
        if b-a == maxv:
            answer.append(rion[::])
        elif b-a > maxv:
            maxv = b-a
            answer = [rion[::]]
        return
    
    for i in range(idx, 11):        
        while(info[i] >= rion[i] and count != n):
            rion[i] += 1
            count += 1
        dfs(n, count, i+1, info, rion)
        count -= rion[i]
        rion[i] = 0


def solution2(n, info):
    answer = []
    maxv = -1
    for case in combinations_with_replacement(range(11), n):
        rion = [0]*11
        for idx in case:
            rion[idx] += 1
        score = 0
        for i in range(11):
            if rion[i] > info[i]:
                score += (10-i)
            elif info[i] != 0:
                score -= (10-i)
        if score <= 0:
            continue
        if score == maxv:
            answer.append(rion[:])
        elif score > maxv:
            maxv = score
            answer = [rion[:]]
    
    if not answer:
        return [-1]
    else:
        tmp = [x[::-1] for x in answer]
        return sorted(tmp)[-1][::-1]

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9,[0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution2(5,[2,1,1,1,0,0,0,0,0,0,0]))
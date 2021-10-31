

def solution(lottos, win_nums):

    rank = [6,6,5,4,3,2,1]
    znum = lottos.count(0)
    match = 0
    for x in lottos:
        if x in win_nums:
            match+=1
    return rank[match+znum],rank[match]


solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19])

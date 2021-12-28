
# https://programmers.co.kr/learn/courses/30/lessons/49994
def solution(dirs):
    answer = 0
    s = set()
    dmap = {
        'U' : [-1,0],
        'R' : [0,1],
        'D' : [1,0],
        'L' : [0,-1]
    }
    x,y = 0,0
    for d in dirs:
        a,b = dmap[d]
        if -5 <= x+a <= 5 and -5 <= y+b <= 5:
            s.add(tuple([min(x,x+a), min(y,y+b), max(x,x+a), max(y,y+b)]))
            x += a
            y += b
    return len(s)
print(solution("UDU"))
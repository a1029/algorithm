import math

# https://programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    answer = [] 
    s = set()
    idx = -1
    for i,w in enumerate(words):
        if w in s:
            idx = i
            break
        s.add(w)
    if idx == -1:
        s = words[0]
        for i,w in enumerate(words[1:],1):
            if s[-1] != w[0]:
                idx = i
                break
            s = w
        if idx == -1:
            return [0,0]
    a = idx % n + 1
    b = math.ceil((idx + 1) / n)
    return [a,b]


def solution2(n, words):
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            return [i%n+1,math.ceil((i+1)/n)]
    return [0,0]

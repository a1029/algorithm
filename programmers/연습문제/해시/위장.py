from functools import reduce
from collections import Counter

def solution(clothes):
    counter = Counter(list(zip(*clothes))[1])
    return reduce(lambda x,y: x*(y+1), counter.values(), 1) -1

def solution2(clothes):
    hashmap = {}
    for _,t in clothes:
        if t in hashmap:
            hashmap[t] += 1
        else:
            hashmap[t] = 2
    answer = 1
    for count in hashmap.values():
        answer *= count
    return answer - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
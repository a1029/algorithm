import re

def solution(s):

    p = re.findall('{(.*?)}', s[1:])
    tmp = []
    for a in p:
        tmp.append(list(map(int, a.split(','))))
    tmp.sort(key=len)
    answer = []
    for nums in tmp:
        for num in nums:
            if num not in answer:
                answer.append(num)
    return answer
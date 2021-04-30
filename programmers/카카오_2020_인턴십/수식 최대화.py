import itertools
import re

def solution(expression):

    arr = re.split('(\D)', expression)
    oper = set(re.findall('\D', expression))

    answer = 0
    for case in itertools.permutations(oper):
        tmp = arr[:]
        for op in case:
            while op in tmp:
                i = tmp.index(op)
                tmp[i-1] = str(eval(tmp[i-1]+tmp[i]+tmp[i+1]))
                tmp.pop(i+1)
                tmp.pop(i)
        answer = max(answer, abs(int(tmp[0])))
    return answer
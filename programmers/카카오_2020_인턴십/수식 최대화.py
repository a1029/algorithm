import itertools
import re

def solution(expression):

    ops = set(re.findall('\D', expression))
    expr = re.split('(\D)', expression)

    answer = 0
    for case in itertools.permutations(ops):
        tmp = expr[:]
        for op in case:
            while op in tmp:
                i = tmp.index(op)
                tmp[i-1] = str(eval(tmp[i-1]+tmp[i]+tmp[i+1]))
                tmp.pop(i+1)
                tmp.pop(i)
        answer = max(answer, abs(int(tmp[0])))
    return answer

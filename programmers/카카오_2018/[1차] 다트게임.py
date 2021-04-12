import re

def solution(dartResult):
    p = re.compile('[\d]+')
    digit = p.findall(dartResult)
    result = []
    cnt = 0
    for i in range(len(dartResult)):
        if dartResult[i]=='S':
            result.append(int(digit[cnt]))
            cnt += 1
        elif dartResult[i]=='D':
            result.append(int(digit[cnt])**2)
            cnt += 1
        elif dartResult[i]=='T':
            result.append(int(digit[cnt])**3)
            cnt += 1
        elif dartResult[i]=='*':
            if cnt==1:
                result[cnt-1]*=2
            else:
                result[cnt-2]*=2
                result[cnt-1]*=2
        elif dartResult[i]=='#':
            result[cnt-1] = -result[cnt-1]

    return sum(result)

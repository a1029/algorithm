from collections import Counter

def solution(a):

    count = Counter(a)
    answer = -1
    for k in count.keys():
        if count[k]<=answer:
            continue
        common_cnt = 0
        i = 0
        while i < len(a)-1:
            if a[i]!=k and a[i+1]!=k or a[i]==a[i+1]:
                i+=1
                continue
            common_cnt += 1
            i+=2
        answer = max(common_cnt, answer)
    if answer==-1:
        return 0
    else:
        return answer*2
from collections import defaultdict

def solution(genres, plays):
    answer = []
    a = defaultdict(int)
    b = defaultdict(list)
    for i in range(len(genres)):
        a[genres[i]] += plays[i]
        b[genres[i]].append([i,plays[i]])
        
    for k in b.keys():
        b[k].sort(key=lambda x: x[1], reverse=True)
        
    for k,v in sorted(a.items(), key=lambda x: x[1], reverse=True):
        if len(b[k]) >= 2:
            for i in range(2):
                answer.append(b[k][i][0])
        else:
            for i in range(len(b[k])):
                answer.append(b[k][i][0])
    
    return answer
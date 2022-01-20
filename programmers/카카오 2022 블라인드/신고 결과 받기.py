from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    s = defaultdict(set)
    for r in report:
        rs = r.split(" ")
        s[rs[1]].add(rs[0])
        
    result = defaultdict(int)
    for a,b in s.items():
        if len(b) >= k:
            for s in b:
                result[s] += 1

    for id in id_list:
        if id in result:
            answer.append(result[id])
        else:
            answer.append(0)

    return answer

def solution2(id_list, report, k):
    answer = [0]*len(id_list)
    s = defaultdict(int)
    for r in set(report):
        s[r.split(" ")[1]] += 1
    
    for r in set(report):
        if s[r.split(" ")[1]] >= k:
            answer[id_list.index(r.split(" ")[0])] += 1
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
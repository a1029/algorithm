import math
from collections import defaultdict
def solution(fees, records):
    answer = []
    r_dict = defaultdict(list)
    t_dict = defaultdict(int)
    for r in records:
        a,b,c = r.split(" ")
        r_dict[b].append([a,c])
        
    for n in r_dict:
        if len(r_dict[n])%2!=0:
            r_dict[n].append(["23:59", "OUT"])
        for i in range(0, len(r_dict[n]), 2):
            t_dict[n] += get_time(r_dict[n][i][0], r_dict[n][i+1][0])
            
    for n in t_dict:
        tmp = fees[1]
        if t_dict[n] > fees[0]:
            tmp += math.ceil((t_dict[n] - fees[0]) / fees[2]) * fees[3]
        answer.append([n,tmp])
            
    return list(zip(*sorted(answer, key=lambda x: x[0])))[1]

def get_time(t1, t2):
    t1 = list(map(int, t1.split(":")))
    t2 = list(map(int, t2.split(":")))
    t1 = t1[0]*60 + t1[1]
    t2 = t2[0]*60 + t2[1]
    return t2-t1


print(solution([180,5000,10,600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
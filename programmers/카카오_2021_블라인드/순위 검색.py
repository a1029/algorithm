from collections import defaultdict
from itertools import combinations
import bisect
def solution(info, query):

    answer = []
    info_dict = defaultdict(list)
    for x in info:
        x = x.split()
        info_key = x[:-1]
        info_val = int(x[-1])
        for i in range(5):
            for c in combinations(info_key, i):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_val)

    for key in info_dict.keys():
        info_dict[key].sort()

    for q in query:
        q_info = q.split(' ')
        q_score = int(q_info[-1])
        q_info = q_info[:-1]

        while 'and' in q_info:
            q_info.remove('and')
        while '-' in q_info:
            q_info.remove('-')
        tmp_q = ''.join(q_info)

        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            index = bisect.bisect_left(scores,q_score)
            answer.append(len(scores)-index)
        else:
            answer.append(0)
    return answer



solution(["java backend junior pizza 150",
          "python frontend senior chicken 210",
          "python frontend senior chicken 150",
          "cpp backend senior pizza 260",
          "java backend junior chicken 80",
          "python backend senior chicken 50"]
         ,["java and backend and junior and pizza 100",
           "python and frontend and senior and chicken 200",
           "cpp and - and senior and pizza 250",
           "- and backend and senior and - 150",
           "- and - and - and chicken 100",
           "- and - and - and - 150"])
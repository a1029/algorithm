
def solution(record):

    dic = {}
    for r in record:
        info = r.split(" ")
        if info[0] in ['Enter', 'Change']:
            dic[info[1]] = info[2]

    answer = []
    for r in record:
        info = r.split(" ")
        if info[0]=="Enter":
            answer.append("%s님이 들어왔습니다." % dic[info[1]])
        elif info[0]=="Leave":
            answer.append("%s님이 나갔습니다." % dic[info[1]])

    return answer

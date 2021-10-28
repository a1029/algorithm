
def solution(relation):

    n,m = len(relation), len(relation[0])
    attr = [x for x in range(m)]
    subset = []
    superkey = []
    for i in range(1<<m):
        tmp = []
        for j in range(m):
            if i & (1<<j):
                tmp.append(attr[j])
        subset.append(tmp)
    subset.pop(0)

    for sub in subset:
        tmp = []
        for i in range(n):
            a = []
            for k in sub:
                a.append(relation[i][k])
            tmp.append(a)
        flag = 0
        for i in range(len(tmp)):
            for j in range(i+1, len(tmp)):
                if tmp[i]==tmp[j]:
                    flag = 1
                    break
            if flag==1:
                break
        if flag==1:
            continue
        else:
            superkey.append(sub)

    superkey.sort(key=lambda x: len(x))
    remove_list = []
    answer = []
    for i in range(len(superkey)):
        for j in range(i+1, len(superkey)):
            if set(superkey[i]) & set(superkey[j]) == set(superkey[i]):
                remove_list.append(superkey[j])
    for key in superkey:
        if key not in remove_list:
            answer.append(key)
    return len(answer)

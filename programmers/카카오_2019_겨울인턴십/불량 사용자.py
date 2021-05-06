import itertools

def check(s1, s2):

    if len(s1)!=(len(s2)):
        return False
    for i in range(len(s1)):
        if s1[i]!=s2[i] and s2[i]!='*':
            return False
    return True

def solution(user_id, banned_id):

    answer = set()
    for case in itertools.permutations(user_id, len(banned_id)):
        count = 0
        for i in range(len(case)):
            if check(case[i],banned_id[i]):
                count += 1
            if count==len(banned_id):
                answer.add(tuple(sorted(case)))
    return len(answer)
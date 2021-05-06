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
    for case in itertools.combinations(user_id, len(banned_id)):
        for perm in itertools.permutations(banned_id):
            count = 0
            for i in range(len(case)):
                if check(case[i],perm[i]):
                    count += 1
            if count==len(banned_id):
                    answer.add(case)
    return len(answer)

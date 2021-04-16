import itertools

def check(a,b):
    if len(a)!=len(b):
        return False
    for i in range(len(a)):
        if b[i]!='*' and a[i]!=b[i]:
            return False
    return True

def solution(user_id, banned_id):

    answer = set()
    for case in itertools.combinations(user_id, len(banned_id)):
        for perm in itertools.permutations(banned_id):
            count = 0
            for i in range(len(case)):
                if check(case[i],perm[i]):
                    count+=1
            if count==len(case):
                answer.add(case)
    return len(answer)

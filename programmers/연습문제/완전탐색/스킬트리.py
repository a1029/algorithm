def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        skill_trees[i] = ''.join(filter(lambda x: x in skill, skill_trees[i]))
    for st in skill_trees:
        flag = False
        for i,s in enumerate(st):
            if st[i] != skill[i]:
                flag = True
        if not flag:
            answer += 1
    return answer
print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))
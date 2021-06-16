
def solution(gems):

    counter = {gems[0]:1}
    left=right=0
    answer = [0,len(gems)-1]
    size = len(set(gems))

    while left<len(gems) and right<len(gems):
        if size==len(counter):
            if right-left < answer[1]-answer[0]:
                answer = [left,right]
            if counter[gems[left]]==1:
                del counter[gems[left]]
            else:
                counter[gems[left]]-=1
            left+=1
        else:
            right+=1
            if right==len(gems):
                break
            if gems[right] in counter.keys():
                counter[gems[right]] += 1
            else:
                counter[gems[right]] = 1

    return [answer[0]+1, answer[1]+1]
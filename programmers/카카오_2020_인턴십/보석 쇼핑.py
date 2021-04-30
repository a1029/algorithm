
def solution(gems):

    dic = {}
    left=right=0
    answer = [0,len(gems)-1]
    size = len(set(gems))
    dic[gems[0]] = 1
    while left<len(gems) and right<len(gems):
        if size==len(dic):
            if right-left < answer[1]-answer[0]:
                answer = [left,right]
            if dic[gems[left]]==1:
                del dic[gems[left]]
            else:
                dic[gems[left]]-=1
            left+=1
        else:
            right+=1
            if right==len(gems):
                break
            if gems[right] in dic.keys():
                dic[gems[right]]+=1
            else:
                dic[gems[right]]=1
    return [answer[0]+1,answer[1]+1]

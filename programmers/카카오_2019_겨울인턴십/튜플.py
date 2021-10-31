
def solution(s):

    s = s[2:-2].split("},{")
    tmp = []
    for c in s:
        tmp.append(list(map(int, c.split(','))))
    tmp.sort(key=len)

    answer = []
    for nums in tmp:
        for num in nums:
            if num not in answer:
                answer.append(num)
    return answer

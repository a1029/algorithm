# https://programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    answer = 0
    people.sort()
    l, r = 0, len(people)-1

    while l <= r:
        if l != r and people[l] + people[r] <= limit:
            l += 1
        r -= 1
        answer += 1
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([1,1,1,1,1,1,100,100], 100))
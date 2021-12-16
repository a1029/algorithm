# 프로그래머스 분류는 그리디지만
# 문제 요구사항은 최솟값을 요구하는데, 이는 그리디와 거리가 멈
# 아래 코드는 완전탐색에 가까움
def solution(name):
    min_move = len(name)-1
    answer = 0
    for i,c in enumerate(name):
        answer += min(ord(c)-ord('A'), ord('Z')-ord(c)+1)
        j = i + 1
        while j < len(name) and name[j] == 'A':
            j += 1
        min_move = min(min_move, i+i+len(name)-j)
    answer += min_move
    return answer
print(solution("JEROEN"))
print(solution("BBABAAAB"))
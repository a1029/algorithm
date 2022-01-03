def solution(N, number):
    answer = 0
    dp = []        
    for i in range(1, 9):
        s = set()
        s.add(int(str(N)*i))
        for j in range(i-1):
            for a in dp[j]:
                for b in dp[-j-1]:
                    s.add(a+b)
                    s.add(a-b)
                    s.add(a*b)
                    if b!=0:
                        s.add(a//b)
        if number in s:
            return i
        dp.append(s)
    return -1

def solution2(N, number):
    dp = [set() for _ in range(8)]
    for i,s in enumerate(dp, 1):
        s.add(int(str(N)*i))

    for i in range(8):
        for j in range(i):
            for a in dp[j]:
                for b in dp[i-j-1]:
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(a*b)
                    if b!=0:
                        dp[i].add(a//b)
        if number in dp[i]:
            return i+1
    return -1

print(solution(5,12))
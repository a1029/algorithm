import sys
sys.setrecursionlimit(10**6)
# https://programmers.co.kr/learn/courses/30/lessons/12945
def solution(n):
    answer = 0
    dp = [0]*(n+1)
    dp[1] = 1
    def fib(a):
        if a <= 1:
            return a
        if dp[a]:
            return dp[a]
        dp[a] = fib(a-2) + fib(a-1)
        return dp[a]
    return fib(n) % 1234567

def solution2(n):
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[-1] % 1234567

def solution3(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
    return a % 1234567
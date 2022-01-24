def solution(n, k):
    answer = 0
    r = get_k(n, k)
    
    for s in r.split("0"):
        if s!='' and is_prime(int(s)):
            answer += 1
        
    return answer

def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def get_k(n, q):
    result = ''
    while n > 0:
        n, mod = divmod(n, q)
        result += str(mod)
        
    return result[::-1]


print(solution(437674, 3))
print(solution(110011, 10))
answer = 0
def solution(numbers, target):
    global answer
    def dfs(total, i, count, length):
        global answer
        if count == length:
            if total == target:
                answer += 1
            return
        dfs(total + numbers[i], i + 1, count + 1, length)    
        dfs(total - numbers[i], i + 1, count + 1, length)
    dfs(0, 0, 0, len(numbers))
    return answer

def solution2(numbers, target):
    q = [0]
    for n in numbers:
        s = []
        for _ in range(len(q)):
            x = q.pop()
            s.append(x + n)
            s.append(x + n*(-1))
            
        q = s.copy()
    return q.count(target)
    
solution([1,1,1,1,1],3)
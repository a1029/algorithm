def solution(a, b, g, s, w, t):
    answer = (10**5) * (10**9) * 2 * 2
    start = 0
    end = (10**5) * (10**9) * 2 * 2
    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0
        for i in range(len(w)):

            move_cnt = mid // (t[i] * 2)
            if mid % (t[i] * 2) >= t[i]:
                move_cnt += 1

            gold += g[i] if g[i] < move_cnt * w[i] else move_cnt * w[i]
            silver += s[i] if s[i] < move_cnt * w[i] else move_cnt * w[i]
            total += g[i] + s[i] if g[i] + s[i] < move_cnt * w[i] else move_cnt * w[i]

        if gold >= a and silver >= b and total >= a + b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
    return answer


print(solution(10,10,[100],[100],[7],[10]))
print(solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1]))
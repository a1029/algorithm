def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
            continue
        tmp = list('0' + bin(num)[2:])
        idx = ''.join(tmp).rfind('0')
        tmp[idx] = '1'
        tmp[idx+1] ='0'
        answer.append(int(''.join(tmp), 2))
    return answer

print(solution([3,7]))
# self-solving : X
def my_answer(s):
    sub_array = []
    temp = []
    # 원소의 길이가 1부터 문자열의 총 길이까지인 부분집합 만들기
    for i in range(len(s)):
        for j in range(0, len(s), i + 1):
            temp.append(s[j:j + (i + 1)])
        sub_array.append(temp[:])
        temp.clear()

    count = 1
    result = ''
    result_array = []
    for a in sub_array:
        # 문자열 비교
        for i in range(1, len(a)):
            # 이전과 같으면 count 증가
            if a[i] == a[i - 1]:
                count += 1
            # 이전과 다르면 count와 이전 문자열 추가
            else:
                result += str(count) + a[i - 1]
                count = 1
        # 마지막 반복된 문자열도 계산
        result += str(count) + a[-1]
        # 1은 생략하므로 제거
        result = result.replace("1", "")

        result_array.append(result)
        result = ''
        count = 1

    return min([len(result) for result in result_array])


def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer


print(my_answer("aabbaccc"))  # 2a2ba3c, 7
print(my_answer("ababcdcdababcdcd"))  # 2ababcdcd, 9
print(my_answer("abcabcdede"))  # 2abcdede, 8
print(my_answer("abcabcabcabcdededededede"))  # 2abcabc2dedede, 14
print(my_answer("xababcdcdababcdcd"))  # xababcdcdababcdcd, 17

print(solution("aabbaccc"))  # 2a2ba3c, 7
print(solution("ababcdcdababcdcd"))  # 2ababcdcd, 9
print(solution("abcabcdede"))  # 2abcdede, 8
print(solution("abcabcabcabcdededededede"))  # 2abcabc2dedede, 14
print(solution("xababcdcdababcdcd"))  # xababcdcdababcdcd, 17

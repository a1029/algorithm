
def solution(words):
    root = {}
    for word in words:
        now = root
        for w in word:
            now.setdefault(w,[0,{}])
            now[w][0] += 1
            now = now[w][1]

    answer = 0
    for word in words:
        now = root
        for i in range(len(word)):
            if now[word[i]][0] == 1:
                break
            now = now[word[i]][1]
        answer += i+1
    return answer

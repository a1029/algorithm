import collections

def solution(msg):
    answer = []
    word_dict = collections.defaultdict(int)
    for i in range(1, 27):
        word_dict[chr(64+i)] = i
    i = 0
    while i < len(msg):
        j = i+1
        while word_dict[msg[i:j]] != 0:
            j += 1
            if j-1 > len(msg):
                break
        answer.append(word_dict[msg[i:j-1]])
        if word_dict[msg[i:j]] == 0:
            word_dict[msg[i:j]] = max(word_dict.values())+1
        i += j-i-1
    return answer

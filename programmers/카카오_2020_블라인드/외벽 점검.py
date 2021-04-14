import itertools

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(n+weak[i])

    answer = len(dist)+1
    for start in range(length):
        for friends in itertools.permutations(dist):
            count = 1
            cur_pos = weak[start] + friends[count-1]
            for nxt in range(start+1, start+length):
                if cur_pos < weak[nxt]:
                    count += 1
                    if count > len(dist):
                        break
                    cur_pos = weak[nxt] + friends[count-1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer
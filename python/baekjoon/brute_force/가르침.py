import collections
import itertools

n, k = map(int, input().split())
words = [input() for i in range(n)]

tmp = []
freqs = collections.defaultdict(int)
for i in range(n):
    for j in range(len(words[i])):
        if words[i][j] not in tmp:
            tmp.append(words[i][j])
            freqs[words[i][j]] += 1
    tmp.clear()

freqs = list(freqs.items())
freqs.sort(key=lambda x:-x[1])
freqs = freqs[:k]

result = 0
for case in itertools.combinations(freqs, k):
    match = 0
    for word in words:
        tmp = 0
        for w,c in case:
            if w in word:
                tmp += 1
        if tmp>=len(set(word)):
            match += 1
    result = max(result, match)
print(result)
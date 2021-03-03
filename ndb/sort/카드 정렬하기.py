import itertools
import heapq

# X
def my_answer(n, data):
    perms = list(itertools.permutations(data))
    result = 1e9
    for perm in perms:
        print(perm)
        compare = perm[0] + perm[1]
        for card in perm[2:]:
            compare += compare + card
        result = min(result, compare)

    print(result)


def solution(n, data):
    q = []
    for a in data:
        heapq.heappush(q, a)

    result = 0

    while len(q) != 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        result += a + b
        heapq.heappush(q, a + b)

    print(result)


my_answer(3, [10, 20, 40])
solution(3, [10, 20, 40])

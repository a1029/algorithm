import itertools

mo = ['a','e','i','o','u']

l, c = map(int, input().split())
data = input().split()
data.sort()

for p in itertools.combinations(data, l):
    count = 0
    for i in p:
        if i in mo:
            count += 1
    if 1 <= count <= l-2:
        print(''.join(p))
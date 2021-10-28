def rotate(n, d):
    isrotate = [False]*4
    direct = [0]*4

    isrotate[n] = True
    direct[n] = d
    tmpd = d
    for i in range(n, 3):
        if gear[i][2] != gear[i+1][6]:
            isrotate[i+1] = True
            direct[i+1] = -tmpd
            tmpd = -tmpd
        else:
            break

    tmpd = d
    for j in range(n, 0, -1):
        if gear[j][6] != gear[j-1][2]:
            isrotate[j-1] = True
            direct[j-1] = -tmpd
            tmpd = -tmpd
        else:
            break

    for k in range(4):
        if isrotate[k]:
            if direct[k] == 1:
                last = gear[k].pop()
                gear[k] = [last] + gear[k]
            else:
                first = gear[k].pop(0)
                gear[k] = gear[k] + [first]

gear = [list(input()) for _ in range(4)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    rotate(a-1, b)
result = 0
for i in range(4):
    if gear[i][0] == '1':
        result += 2**i
print(result)

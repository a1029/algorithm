n, m = map(int, input().split())
arr = [input() for _ in range(n)]
result = int(1e9)

for i in range(n-7):
    for j in range(m-7):
        white = 0
        black = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if arr[a][b] != 'W':
                        white += 1
                    if arr[a][b] != 'B':
                        black += 1
                else:
                    if arr[a][b] != 'B':
                        white += 1
                    if arr[a][b] != 'W':
                        black += 1
        result = min(result, white, black)

print(result)

def rotate(key):
    n = len(key)
    new_key = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_key[j][n-1-i] = key[i][j]
    return new_key

def check(new_lock):
    a = len(new_lock)//3
    for i in range(a, a*2):
        for j in range(a, a*2):
            if new_lock[i][j]!=1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for _ in range(4):
        key = rotate(key)
        for a in range(n*2):
            for b in range(n*2):
                for c in range(m):
                    for d in range(m):
                        new_lock[a+c][b+d] += key[c][d]
                if check(new_lock):
                    return True
                for c in range(m):
                    for d in range(m):
                        new_lock[a+c][b+d] -= key[c][d]
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

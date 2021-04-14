
def turn(key):
    m = len(key)
    new_key = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            new_key[j][m-1-i] = key[i][j]
    return new_key

def check(new_lock):
    n = len(new_lock)//3
    for i in range(n):
        for j in range(n):
            if new_lock[i+n][j+n]!=1:
                return False
    return True

def solution(key, lock):
    m,n = len(key), len(lock)
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for a in range(n*2):
        for b in range(n*2):
            for _ in range(4):
                key = turn(key)
                for c in range(m):
                    for d in range(m):
                        new_lock[a+c][b+d] += key[c][d]
                if check(new_lock):
                    return True
                for c in range(m):
                    for d in range(m):
                        new_lock[a+c][b+d] -= key[c][d]
    return False
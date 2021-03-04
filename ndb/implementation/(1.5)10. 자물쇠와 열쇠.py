from typing import List


# X
# 2차원 리스트 90도 시계방향 회전
def rotate(key: List[List[int]]):
    col = len(key)
    row = len(key[0])
    result = [[0] * col for _ in range(row)]
    for i in range(col):
        for j in range(row):
            result[j][col - i - 1] = key[i][j]
    return result


# 새로운 자물쇠 중앙이 모두 1인지 확인
def check(new_lock: List[List[int]]):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠 크기 3배 확장
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 기존 자물쇠를 새로운 자물쇠의 중앙으로 이동
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해
    for rotation in range(4):
        key = rotate(key)
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))


# X
def my_answer(build_frame):
    result = set()
    count = 0
    count2 = 0
    for x, y, a, b in build_frame:
        # 기둥설치
        if a == 0 and b == 1:
            # 바닥에 설치
            if y == 0:
                result.add((x, y, a))
                continue
            for i, j, k in result:
                # 기둥의 위끝에 설치
                if k == 0 and [x, y] == [i, j + 1]:
                    result.add((x, y, a))
                    break
                # 보의 양 끝에 설치
                if (k == 1 and [x, y] == [i, j]) or (k == 1 and [x, y] == [i + 1, j]):
                    result.add((x, y, a))
                    break

        # 보설치
        elif a == 1 and b == 1:
            for i, j, k in result:
                # 기둥의 끝에 설치
                if k == 0 and [x, y] == [i, j + 1]:
                    result.add((x, y, a))
                    break
                # 보 사이에 설치
                if k == 1 and [x, y] == [i + 1, j]:
                    count += 1
                elif k == 1 and [x + 1, y] == [i, j]:
                    count += 1
                if count == 2:
                    result.add((x, y, a))
                    count = 0
                    break
                # 왼쪽은 보, 오른쪽은 기둥의 끝인 곳에 설치
                if k == 1 and [x, y] == [i + 1, j]:
                    count2 += 1
                elif k == 0 and [x + 1, y] == [i, j + 1]:
                    count2 += 1
                if count2 == 2:
                    result.add((x, y, a))
                    count2 = 0
                    break

    result = sorted(result, key=lambda x: (x[0], x[1]))
    print(result)


def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif stuff == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    print(sorted(answer))


solution(
    [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
     [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]])
solution(
    [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1],
     [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
     [1, 1, 1, 0], [2, 2, 0, 1]])

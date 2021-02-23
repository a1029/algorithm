import itertools

# success
# 한 집의 치킨거리 구하기
def cal_distance(i, j, chicks):
    result = 10000
    for a, b in chicks:
        result = min(result, abs(i - a) + abs(j - b))
    return result


def my_answer(n, m, city):
    result = 10000
    chick_distance = 0
    chicks = []
    homes = []
    # 집과 치킨집의 모든 좌표 구하기
    for i in range(len(city)):
        for j in range(len(city[0])):
            if city[i][j] == 1:
                homes.append([i, j])
            if city[i][j] == 2:
                chicks.append([i, j])

    # 치킨집 조합 구하기
    sub_chicks = list(itertools.combinations(chicks, m))

    # 각 치킨집 조합에 대해
    for chicks in sub_chicks:
        # 각 도시에 대해
        for i, j in homes:
            # 도시의 치킨 거리 구하기
            chick_distance += cal_distance(i, j, chicks)
        result = min(result, chick_distance)
        chick_distance = 0

    print(result)


my_answer(5, 3,
         [[0, 0, 1, 0, 0],
          [0, 0, 2, 0, 1],
          [0, 1, 2, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 0, 2]])
my_answer(5, 2,
         [[0, 2, 0, 1, 0],
          [1, 0, 1, 0, 0],
          [0, 0, 0, 0, 0],
          [2, 0, 0, 1, 1],
          [2, 2, 0, 1, 2]])
my_answer(5, 1,
         [[1, 2, 0, 0, 0],
          [1, 2, 0, 0, 0],
          [1, 2, 0, 0, 0],
          [1, 2, 0, 0, 0],
          [1, 2, 0, 0, 0]])
my_answer(5,1,
          [[1,2,0,2,1],
           [1,2,0,2,1],
           [1,2,0,2,1],
           [1,2,0,2,1],
           [1,2,0,2,1]])
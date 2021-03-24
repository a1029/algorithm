from typing import List


def my_answer(input: List[str]):

    def dfs(i, j):

        if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[i]) or arr[i][j] == '1':
            return

        arr[i][j] = '1'

        dfs(i + 1, j)
        dfs(i, j + 1)
        dfs(i - 1, j)
        dfs(i, j - 1)

    result = 0
    arr = []
    for line in input:
        arr.append(list(line))

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != '1':
                dfs(i, j)
                result += 1

    print(result)



def solution(input: List[str]):

    def dfs(i, j):

        if i <= -1 or i >= len(arr) or j <= -1 or j >= len(arr[i]):
            return False
        if arr[i][j] == '0':
            arr[i][j] = '1'

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
            return True
        return False

    result = 0
    arr = []
    for line in input:
        arr.append(list(line))

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if dfs(i, j) == True:
                result += 1

    print(result)


my_answer(['00110',
             '00011',
             '11111',
             '00000'])
solution(['00110',
            '00011',
            '11111',
            '00000'])
my_answer(['00000111100000',
             '11111101111110',
             '11011101101110',
             '11011101100000',
             '11011111111111',
             '11011111111100',
             '11000000011111',
             '01111111111111',
             '00000000011111',
             '01111111111000',
             '00011111111000',
             '00000001111000',
             '11111111110011',
             '11100011111111',
             '11100011111111'])
solution(['00000111100000',
            '11111101111110',
            '11011101101110',
            '11011101100000',
            '11011111111111',
            '11011111111100',
            '11000000011111',
            '01111111111111',
            '00000000011111',
            '01111111111000',
            '00011111111000',
            '00000001111000',
            '11111111110011',
            '11100011111111',
            '11100011111111'])

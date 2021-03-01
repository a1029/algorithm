import itertools


# success
def cal(array):
    result = array[0]
    for i in range(1, len(array) - 1):
        if array[i] == '+':
            result += array[i + 1]
        elif array[i] == '-':
            result -= array[i + 1]
        elif array[i] == '*':
            result *= array[i + 1]
        elif array[i] == '/':
            if result < 0:
                result = -(-result // array[i + 1])
            else:
                result //= array[i + 1]
    return result


def my_answer(n, data, data2):
    expand = [''] * (len(data) * 2 - 1)
    operate = ['+', '-', '*', '/']
    perm = []
    result = []
    for i in range(len(data)):
        expand[i * 2] = data[i]
    for i, op in enumerate(data2):
        for j in range(op):
            perm.append(operate[i])
    perm = list(itertools.permutations(perm))

    for p in perm:
        for i in range(len(p)):
            expand[i * 2 + 1] = p[i]

        result.append(cal(expand))
    print(max(result), min(result))


class Solution:
    min_value = 1e9
    max_value = -1e9
    add, sub, mul, div = 0, 0, 0, 0

    def solution(self, n, data, data2):

        self.add, self.sub, self.mul, self.div = data2

        def dfs(i, now):
            if i == n:
                self.min_value = min(self.min_value, now)
                self.max_value = max(self.max_value, now)
            else:
                if self.add > 0:
                    self.add -= 1
                    dfs(i + 1, now + data[i])
                    self.add += 1
                if self.sub > 0:
                    self.sub -= 1
                    dfs(i + 1, now - data[i])
                    self.sub += 1
                if self.mul > 0:
                    self.mul -= 1
                    dfs(i + 1, now * data[i])
                    self.mul += 1
                if self.div > 0:
                    self.div -= 1
                    dfs(i + 1, int(now / data[i]))
                    self.div += 1

        dfs(1, data[0])
        print(self.max_value, self.min_value)


p = Solution()
p.solution(2, [5, 6], [0, 0, 1, 0]) # 30 30
p.solution(3, [3, 4, 5], [1, 0, 1, 0]) # 35 17
p.solution(6, [1, 2, 3, 4, 5, 6], [2, 1, 1, 1]) # 54 -24

my_answer(2, [5, 6], [0, 0, 1, 0])
my_answer(3, [3, 4, 5], [1, 0, 1, 0])
my_answer(6, [1, 2, 3, 4, 5, 6], [2, 1, 1, 1])

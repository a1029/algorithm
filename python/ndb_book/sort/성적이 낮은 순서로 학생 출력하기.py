from typing import List

n = int(input())
arr = []
for i in range(n):
    input_data = input().split()
    arr.append((input_data[0], int(input_data[1])))
arr.sort()

for name, score in arr:
    print(name, end=' ')
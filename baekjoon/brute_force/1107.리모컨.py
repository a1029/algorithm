n = int(input())
m = int(input())
broken = set()
if m>0: broken = set(input().split())
result = abs(100-n)
for num in range(1000001):
    num = str(num)
    for j in range(len(num)):
        if num[j] in broken:
            break
        elif j==len(num)-1:
            result = min(result, abs(n-int(num)) + len(num))
print(result)

'''n = list(map(int, input()))
m = int(input())
broken = []
if m > 0:
    broken = list(map(int, input().split()))
result = abs(int(''.join(map(str, n)))-100)
result2 = 0
tmp = []
for i in n:
    if i not in broken:
        tmp.append(i)
for i in tmp:
    n.remove(i)
    result2 += 1
result2 += len(n)
tmp = ""
for i in n:
    for j in range(1, 11):
        if i+j<10:
            if i+j not in broken:
                tmp += str(i+j)
                break
        if i-j>-1:
            if i-j not in broken:
                tmp += str(i-j)
                break
result2 += abs(int(''.join(map(str, n))) - int(tmp))
print(min(result2, result))'''
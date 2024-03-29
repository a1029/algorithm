
n = int(input())
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True


def dfs(num):
    if len(str(num))==n:
        print(num)
        return
    for i in range(10):
        tmp = num*10+i
        if is_prime(tmp):
            dfs(tmp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)
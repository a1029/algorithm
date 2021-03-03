from typing import List

# O
def my_answer(n, arr: List[str]):

    i,j=1,1
    for d in arr:
        if d=='L':
           if j>=2:
               j-=1
        elif d=='R':
            if j<=n-1:
                j+=1
        elif d=='U':
            if i>=2:
                i-=1
        elif d=='D':
            if i<=n-1:
                i+=1

    print([i,j])

def solution(n, arr: List[str]):

    x,y=1,1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    move_types = ['L','R','U','D']

    for plan in arr:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx<1 or ny<1 or nx>n or ny>n:
            continue
        x,y = nx,ny

    print(x,y)

my_answer(5, ['R','R','R','U','D','D'])
solution(5, ['R','R','R','U','D','D'])
my_answer(5, ['D','D','L','R','R','R', 'U', 'L', 'D','D','D'])
solution(5, ['D','D','L','R','R','R', 'U', 'L', 'D','D','D'])
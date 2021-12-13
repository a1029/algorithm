tc = int(input())
for _ in range(tc):
    n = int(input())
    waters = list(map(int, input().split()))
    is_watered = False
    is_die = False
    count = 0
    tall = 1
    for w in waters:
        if w == 1:
            count = 0
            if is_watered:
                tall += 5
            else:
                tall += 1
            is_watered = True
        else:
            is_watered = False
            count += 1
            if count == 2:
                is_die = True
                break
    if is_die:
        print(-1)
    else:
        print(tall)


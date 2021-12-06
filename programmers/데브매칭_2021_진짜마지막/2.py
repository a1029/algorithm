from collections import defaultdict

def solution(n, recipes, orders):
    answer = 0
    cook_num = defaultdict(int)
    cook_map = {}
    cooking = []
    for i in range(len(recipes)):
        tmp = recipes[i].split(" ")
        cook_map[tmp[0]] = int(tmp[1])

    for i in range(len(orders)):
        tmp = orders[i].split(" ")
        name = tmp[0]
        time = tmp[1]
        num = cook_num[name]
        orders[i] = [tmp[0]+str(num), int(tmp[1])]
        cook_num[name] = num + 1

    waiting = orders[::]
    curr_time = 0
    last_cook = orders[len(orders)-1][0]

    while True:
        curr_time += 1
        remove_list = []
        for i, [name, time] in enumerate(cooking):
            time -= 1
            if time<=0 and name==last_cook:
                return curr_time
            if time<=0:
                remove_list.append([name, time])
            cooking[i] = [name, time]
        
        for name, time in remove_list:
            index = cooking.index([name, time])
            cooking.pop(index)
          
        for i, [name, time] in enumerate(waiting):
            if(len(cooking)<n and curr_time >= time):
                new_name = ''.join([c for c in name if not c.isdigit()])
                cooking.append([name, cook_map[new_name]])
                waiting.pop(i)
                break

    return curr_time

print(solution(2, ["A 3","B 2"], ["A 1","A 2","B 3","B 4"]))
print(solution(3, ["SPAGHETTI 3", "FRIEDRICE 2", "PIZZA 8"], ["PIZZA 1", "FRIEDRICE 2", "SPAGHETTI 4", "SPAGHETTI 6", "PIZZA 7", "SPAGHETTI 8"]))
print(solution(1, ["COOKIE 10000"], ["COOKIE 300000"]))


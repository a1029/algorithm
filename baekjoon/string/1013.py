import re
t = int(input())
p = re.compile('(100+1+|01)+')
for _ in range(t):
    string = input()
    result = p.fullmatch(string)
    if result:
        print("YES")
    else:
        print("NO")
    

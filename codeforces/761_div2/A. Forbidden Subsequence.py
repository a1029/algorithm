from collections import defaultdict
tc = int(input())
for _ in range(tc):
    s = input()
    t = input()
    count_dict = defaultdict(int)
    for c in sorted(set(s)):
        count_dict[c] = s.count(c)
    need = ''
    flag = False
    for c in t:
        if c not in s:
            flag = True
            break

    need = ''
    answer = ''
    if flag:
        print(''.join(sorted(s)))
    else:
        if t[0] == 'a':
            need = 'a' + t[2] + t[1]
        else:
            need = 'abc'
        for c in need:
            count = count_dict[c]
            while count != 0:
                count -= 1
                answer += c
            del count_dict[c]
        
        for c in count_dict:
            count = count_dict[c]
            while count != 0:
                count -= 1
                answer += c
        print(answer)
        

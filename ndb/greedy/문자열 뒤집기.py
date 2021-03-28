s = input()
a,b=0,0
if s[0]=='1':
    a+=1
    flag = 1
else:
    b+=1
    flag = 0
for i in range(1, len(s)):
    if s[i]=='0' and flag==1:
        b+=1
        flag = 0
    elif s[i]=='1' and flag==0:
        a+=1
        flag = 1
print(min(a,b))
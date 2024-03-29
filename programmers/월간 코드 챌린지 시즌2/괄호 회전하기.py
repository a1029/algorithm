def check(s):
    stack = []
    for c in s:
        if len(stack)==0 and (c==']' or c==')' or c=='}'):
            return False
        if c=='[' or c=='(' or c=='{':
            stack.append(c)
        else:
            if c==']' and stack[-1]=='[':
                stack.pop()
            elif c==')' and stack[-1]=='(':
                stack.pop()
            elif c=='}' and stack[-1]=='{':
                stack.pop()
    if len(stack)==0:
        return True
    else:
        return False

def solution(s):
    answer = 0
    for x in range(len(s)):
        tmp = s[x:] + s[:x]
        if check(tmp):
            answer+=1
    return answer

'''
def check(s):
    a=b=c=0
    for char in s:
        if char=='[':
            a+=1
        elif char=='{':
            b+=1
        elif char=='(':
            c+=1
        elif char==']':
            a-=1
        elif char=='}':
            b-=1
        elif char==')':
            c-=1
        if a<0 or b<0 or c<0:
            return False
    if a==b==c==0:
        return True
    else:
        return False
        
def solution(s):
    answer = 0
    for x in range(len(s)):
        tmp = s[x:] + s[:x]
        if check(tmp):
            answer+=1
    return answer
'''
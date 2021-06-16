
def check(s):
    count = 0
    for c in s:
        if c=='(':
            count+=1
        else:
            count-=1
            if count<0:
                return False
    return True

def separate(w):
    a,b=0,0
    for c in w:
        if c=='(':
            a+=1
        else:
            b+=1
        if a==b:
            return w[:(a+b)], w[(a+b):]

def solution(p):

    if p=="":
        return ""

    u,v = separate(p)
    if check(u):
        u += solution(v)
        return u
    else:
        tmp = "("
        tmp += solution(v)
        tmp += ")"
        for c in u[1:-1]:
            if c=='(':
                tmp += ')'
            else:
                tmp += '('
        return tmp




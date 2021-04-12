
def solution(n, t, m, p):

    tmp = "0123456789ABCDEF"
    def convert(num, base):
        q,r = divmod(num,base)
        if q==0:
            return tmp[r]
        else:
            return convert(q,base) + tmp[r]

    answer = ''
    result = []
    for i in range(t*m):
        result.extend(convert(i,n))
    i = p-1
    while len(answer)!=t:
        answer += result[i]
        i+=m

    return answer
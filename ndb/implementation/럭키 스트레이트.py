
# O
def my_answer(num):

    num = [int(n) for n in str(num)]
    mid = len(num)//2
    if sum(num[0:mid])==sum(num[mid:len(num)]):
        return "LUCKY"
    else:
        return "READY"


print(my_answer(123402)) # LUCKY
print(my_answer(7755)) # READY

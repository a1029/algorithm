
# O
def my_answer(data: str):

    str_array = []
    num_array = []
    for s in data:
        if s.isalpha():
            str_array.append(s)
        else:
            num_array.append(int(s))

    return ''.join(sorted(str_array))+str(sum(num_array))


print(my_answer("K1KA5CB7")) # ABCKK13
print(my_answer("AJKDLSI412K4JSJ9D")) # ADDIJJJKKLSS20
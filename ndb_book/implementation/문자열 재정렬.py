
# O
data = input()
str_array = []
num_array = []
for s in data:
    if s.isalpha():
        str_array.append(s)
    else:
        num_array.append(int(s))

print(''.join(sorted(str_array))+str(sum(num_array)))
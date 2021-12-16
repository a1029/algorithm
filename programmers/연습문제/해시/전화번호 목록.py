def solution(phone_book):
    answer = True
    phone_book.sort()
    for a,b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    return True

def solution2(phone_book):
    hash_map = {}
    for p in phone_book:
        hash_map[p] = 1
    for p in phone_book:
        tmp = ""
        for n in p:
            tmp += n
            if tmp in hash_map and tmp != p:
                return False
    return True
print(solution2(["119", "97674223", "1195524421"]))
print(solution2(["123","456","789"]))
print(solution2(["12","123","1235","567","88"]))

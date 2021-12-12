import itertools
import collections

def solution(orders, course):

    answer = []
    for k in course:
        tmp = []
        for order in orders:
            for case in itertools.combinations(order, k):
                tmp.append(''.join(sorted(case)))
        menu_count = collections.Counter(tmp).most_common()
        answer += [m for m,c in menu_count if c>=2 and c==menu_count[0][1]]
    return sorted(answer)


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])
solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5])
solution(["XYZ", "XWY", "WXA"],[2,3,4])
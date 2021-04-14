import re

def solution(word, pages):

    pageinfo = []
    for page in pages:
        tmp = {}
        tmp['url'] = re.search('<meta property="og:url" content="(.*?)"/>', page).group(1)

        links = re.findall('<a href="(.*?)">', page)
        tmp['links'] = links
        tmp['out'] = len(links)

        tmp['basic'] = re.sub("[^a-z]", ".", page.lower()).split('.').count(word.lower())
        tmp['matching'] = tmp['basic']
        pageinfo.append(tmp)

    for i in range(len(pageinfo)):
        for j in range(len(pageinfo)):
            if i != j:
                for link in pageinfo[j]['links']:
                    if pageinfo[i]['url'] == link:
                        pageinfo[i]['matching'] += pageinfo[j]['basic'] / pageinfo[j]['out']
                        break

    answer = []
    for i,info in enumerate(pageinfo):
        answer.append([info['matching'],i])
    answer.sort(key=lambda x:(-x[0],x[1]))
    return answer[0][1]

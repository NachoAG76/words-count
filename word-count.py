import sys
import os

reload(sys)
sys.setdefaultencoding("utf-8")
ignores = ['for', 'to', 'the', 'of', 'on', 'that', 'are', 'can', 'be', 'this', 'is', 'from', 'by', 'and']


def analysis(fileName):
    dic = {}
    for i in open('input/' + fileName + '.txt', 'rb'):
        i = i.strip().lower()
        array = i.split()
        for j in array:
            if not dic.has_key(j):
                dic[j] = 0
            dic[j] += 1
    return dic


def output(dic, fileName):
    path = 'output/' + fileName + ' Result' + '.txt'
    if os.path.isfile(path):
        os.remove(path)
    f = open(path, 'w')
    sorteds = sorted(dic, key=dic.__getitem__, reverse=True)

    for i in sorteds:
        if not i in ignores:
            f.write(i + '\t' + str(dic[i]) + '\n')
    f.close()


def union(dict1, dict2):
    dict3 = {}
    for d1 in dict1:
        if dict2.has_key(d1):
            dict3[d1] = dict1[d1] + dict2[d1]
        else:
            dict3[d1] = dict1[d1]

    for d2 in dict2:
        if not dict1.has_key(d2):
            dict3[d2] = dict2[d2]
    return dict3


files = ['Companionship of Books',
         'Just for Today',
         'My Father',
         'test']

dics = {}
for f in files:
    dic = analysis(f)
    output(dic, f)
    dics = union(dics, dic)

output(dics, "total result")

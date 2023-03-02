# group_by 6.5.1
from collections import defaultdict


def group_by(func, lst):
    d = defaultdict(list)

    for item in lst:
        d[func(item)].append(item)

    return d

a = group_by(len, ["23","hjk","23","hjk","l"])
print (a)
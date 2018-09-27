import collections


def lion(pop):
    new = collections.Counter(pop)
    lis = []
    for n, m in new.items():
        if m == 1:
            lis.append(n)
    return lis


q = lion("ghkadhkdhadj")

print(q) 
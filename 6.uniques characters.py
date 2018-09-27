import collections


def give(sentence):
    new = collections.Counter(sentence)
    lis = []
    for n, m in new.items():
        if m == 1:
            lis.append(n)
    return lis


ans = give("I like working for Jyroo because I like the problem they are solving. "
         "Good education lays a strong foundation for a brighter tomorrow")

print(ans)
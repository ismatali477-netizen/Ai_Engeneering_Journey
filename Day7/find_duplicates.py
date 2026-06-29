from collections import Counter
def find_duplicates(l):
    l1 = []
    d = Counter(l)
    for item in set(l):
        if d[item] > 1:
            l1.append(item)
    return l1
print(find_duplicates([1,1,2,2,2,3]))

from collections import Counter
def first_unique(l):
    d=Counter(l)
    for num in l:
        if d[num]==1:
            return num
    else:
        return None
print(first_unique([2,3,2,3]))

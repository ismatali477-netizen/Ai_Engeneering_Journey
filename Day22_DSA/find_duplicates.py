from collections import Counter
def find_duplicates(l):
    d=Counter(l)
    return [item for item in d if d[item]>1]
print(find_duplicates([4,3,2,7,8,2,3,1]))

from collections import Counter
def first_unique_char(s):
    d=dict(Counter(s))
    for item in d:
        if d[item]==1:
            return item
    else:
        return None
print(first_unique_char("aabbcdde"))

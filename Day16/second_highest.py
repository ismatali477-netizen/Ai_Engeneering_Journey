def second_highest(l):
    s=sorted(set(l))
    return s[-2]
print(second_highest([1, 5, 3, 5, 2]))

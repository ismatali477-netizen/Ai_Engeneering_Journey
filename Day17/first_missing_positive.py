def first_missing_positive(l):
    s=set(l)
    for i in range(1,len(s)+2):
        if i not in s:
            return i
print(first_missing_positive([1,2,3]))

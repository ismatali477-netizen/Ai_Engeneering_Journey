def missing_number(l):
    s=set(l)
    s1=set(range(1,len(l)+2))
    return (s1-s).pop()
print(missing_number([1, 2, 4]))

def merge_sorted(m,n):
    l=[]
    for item in m:
        l.append(item)
    for item in n:
        l.append(item)
    return sorted(l)
print(merge_sorted([10,10,30], [20,40]))

def two_sum(l,n):
    seen=set()
    for item in l:
        complement=n-item
        if complement in seen:
            return True
        seen.add(item)
    return False
print(two_sum([1,2,3,4], 8))

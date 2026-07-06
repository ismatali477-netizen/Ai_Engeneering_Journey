def two_sum(l,n):
    d={}
    for i,item in enumerate(l):
        complement=n-item
        if complement in d:
            return [d[complement],i]
        d[item]=i
    return None

print(two_sum([3,2,4], 6))

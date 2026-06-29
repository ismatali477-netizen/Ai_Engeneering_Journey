def group_even_odd(l):
    e,o=[],[]
    result=[e.append(x) if x%2==0 else o.append(x) for x in l]
    return {"Even":e,"odd":o}
print(group_even_odd([1,2,3,4,5]))

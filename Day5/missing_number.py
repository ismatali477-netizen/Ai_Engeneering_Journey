def missing_number(l):
    result=0
    l1=list(range(1,max(l)+1))
    for item1 in l1:
        if item1 not in l:
            result=item1
    return result
print(missing_number([1,2,4,5]))

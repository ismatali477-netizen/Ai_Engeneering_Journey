def second_largest(list):
    l1=[]
    for num in list:
       if num not in l1:
           l1.append(num)
    sort=sorted(l1)
    return sort[(len(sort)-2)]

print(second_largest([10,10,5,3]))

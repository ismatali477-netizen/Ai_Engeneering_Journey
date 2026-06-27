def remove_duplicates(l):
    l1=[]
    for num in l:
       if num not in l1:
           l1.append(num)
    return l1

print(remove_duplicates([1,2,2,2,2,3]))

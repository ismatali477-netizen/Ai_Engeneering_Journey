def remove_duplicates(l):
    l1=[]
    left=0
    for right in range(1,len(l)):
        if l[left]!=l[right]:
            l1.append(l[left])
            left=right
    l1.append(l[left])
    return l1
print(remove_duplicates([1,1,2,2,3]))

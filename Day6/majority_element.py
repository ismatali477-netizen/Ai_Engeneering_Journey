def majority_element(l):
    l1=set(l)
    for item in l1:
        n=l.count(item)
        if n==1:
            continue
        elif n>len(l)//2:
            return item
print(majority_element([2,2,1,2]))

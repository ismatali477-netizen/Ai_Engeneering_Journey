def common_elements(m,n):
    l=[]  #or using set like return list(set(m)&set(n))
    for i in m:
        for j in n:
            if i==j:
                l.append(i)
    l1=[]
    for num in l:
       if num not in l1:
           l1.append(num)
    return l1
print(common_elements([1,1,2], [1,2,2]))

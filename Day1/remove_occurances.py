def repeat(list,n):
    for i in range(len(list)):
        if n in list:
            list.remove(n)
    return list
print(repeat([2,3,3,3,4],3))

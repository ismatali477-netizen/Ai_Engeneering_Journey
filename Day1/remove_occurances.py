def removeOccurance(list,n):
    for i in range(len(list)):
        if n in list:
            list.remove(n)
    return list
print(removeOccurance([2,3,3,3,4],3))
